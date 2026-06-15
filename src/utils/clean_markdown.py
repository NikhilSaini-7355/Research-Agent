import re


def clean_markdown(markdown: str) -> str | None:
    """
    Generic markdown cleaner for RAG systems.

    Removes:
    - Images
    - Markdown URLs
    - Citation exports
    - Social links
    - Navigation noise
    - CTA buttons
    - Footer content
    - Empty tables
    - Login/signup sections

    Returns:
        Cleaned text or None if document is too small.
    """

    text = markdown

    # ==========================================================
    # REMOVE IMAGES
    # ==========================================================

    image_patterns = [
        r"!\[.*?\]\(.*?\)",
        r"\[!\[.*?\]\(.*?\)\]\(.*?\)",
        r"<Base64-Image-Removed>",
    ]

    for pattern in image_patterns:
        text = re.sub(
            pattern,
            "",
            text,
            flags=re.IGNORECASE
        )

    # ==========================================================
    # KEEP LINK TEXT, REMOVE URLS
    # ==========================================================

    text = re.sub(
        r"\[([^\]]+)\]\([^)]+\)",
        r"\1",
        text
    )

    # ==========================================================
    # REMOVE WIKIPEDIA STYLE CITES
    # ==========================================================

    text = re.sub(r"\[\d+\]", "", text)
    text = re.sub(r"\[\[\d+\]\]", "", text)

    # ==========================================================
    # REMOVE COMMON NOISE BLOCKS
    # ==========================================================

    patterns = [

        # Download / Share / Subscribe
        r"\[Download.*?\]",
        r"\[Share.*?\]",
        r"\[Subscribe.*?\]",
        r"\[Print.*?\]",
        r"\[Listen.*?\]",

        # Login / Account
        r"Sign In",
        r"Log In",
        r"Create Account",
        r"Forgot Password",

        # Policies
        r"Privacy Policy",
        r"Privacy Notice",
        r"Cookie Policy",
        r"Cookie Settings",
        r"Terms of Service",
        r"Terms & Conditions",

        # Footnotes
        r"#\s*Footnotes",
        r"##\s*References[\s\S]*",

        # Citation exports
        r"##\s*Cite\s*this[\s\S]*",
        r"##\s*Documents\s*and\s*Links[\s\S]*",
        r"@book\{[\s\S]*?\}",
        r"TY\s*-\s*BOOK[\s\S]*",

        # Empty tables
        r"\|\s*\[\]\(.*?\)",
        r"\|\s*---.*",
        r"\|[\s\xA0]*\|[\s\xA0]*\|",
    ]

    for pattern in patterns:
        text = re.sub(
            pattern,
            "",
            text,
            flags=re.IGNORECASE
        )

    # ==========================================================
    # REMOVE SOCIAL MEDIA LINES
    # ==========================================================

    social_keywords = [
        "facebook",
        "linkedin",
        "instagram",
        "youtube",
        "twitter",
        "x.com",
        "follow us",
        "share this"
    ]

    filtered_lines = []

    for line in text.splitlines():

        if any(
            keyword in line.lower()
            for keyword in social_keywords
        ):
            continue

        filtered_lines.append(line)

    text = "\n".join(filtered_lines)

    # ==========================================================
    # REMOVE CTA / MARKETING LINES
    # ==========================================================

    bad_phrases = [

        "get started",
        "learn more",
        "read more",
        "book a demo",
        "request a demo",
        "try now",
        "contact sales",
        "contact us",
        "sign up",
        "register now",
        "download now",
        "free trial",
        "generate your report",
        "unlock deeper insights",
        "view more",
        "see more",
        "explore more",
        "customer events",
        "share your shopping list"
    ]

    filtered_lines = []

    for line in text.splitlines():

        line_lower = line.lower().strip()

        if any(
            phrase in line_lower
            for phrase in bad_phrases
        ):
            continue

        filtered_lines.append(line)

    text = "\n".join(filtered_lines)

    # ==========================================================
    # FOOTER DETECTION
    # ==========================================================

    footer_patterns = [

        r"contact\s+us",
        r"privacy\s+policy",
        r"privacy\s+notice",
        r"cookie\s+settings",
        r"all\s+rights\s+reserved",
        r"copyright",
        r"modern\s+slavery",
        r"provider\s+information",

    ]

    cut_positions = []

    for pattern in footer_patterns:

        match = re.search(
            pattern,
            text,
            flags=re.IGNORECASE
        )

        if match:
            cut_positions.append(
                match.start()
            )

    if cut_positions:
        text = text[:min(cut_positions)]

    # ==========================================================
    # REMOVE VERY SHORT JUNK LINES
    # ==========================================================

    filtered_lines = []

    for line in text.splitlines():

        line = line.strip()

        if len(line) < 3:
            continue

        filtered_lines.append(line)

    text = "\n".join(filtered_lines)

    # ==========================================================
    # WHITESPACE NORMALIZATION
    # ==========================================================

    text = re.sub(
        r"[ \t]+",
        " ",
        text
    )

    text = re.sub(
        r"\n{3,}",
        "\n\n",
        text
    )

    text = re.sub(
        r"\n\s+\n",
        "\n\n",
        text
    )

    text = text.strip()

    # ==========================================================
    # QUALITY FILTER
    # ==========================================================

    if len(text.split()) < 150:
        return None

    return text