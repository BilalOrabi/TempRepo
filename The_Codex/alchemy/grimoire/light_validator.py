from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = light_spell_allowed_ingredients()
    ingredients_lower = ingredients.lower()

    for i in allowed:
        if i in ingredients_lower:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
