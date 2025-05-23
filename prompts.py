from datetime import datetime

def generate_insight(name, birthdate, birthtime, zodiac, question):
    birth_str = f"{birthdate.strftime('%B %d, %Y')} at {birthtime.strftime('%H:%M')}"
    zodiac_info = f"Your zodiac sign is {zodiac}." if zodiac != "Prefer not to say" else ""

    # This is where you would normally fetch from an astrology API
    astrology_mock = (
        f"Based on the position of celestial bodies, the energy around you "
        f"points toward a period of introspection and renewal. Favorable days ahead."
    )

    response = (
        f"{name}, born on {birth_str}. {zodiac_info}\n\n"
        f"Your question: "{question}"

"
        f"{astrology_mock}

"
        "🌙 This insight is AI-generated for entertainment and reflection purposes."
    )
    return response
