def split_rule_definition(rule_definition: str) -> dict[str, str]:
    """Split rule definition into constituent parts: target, result, context, and exception."""
    rule_parts: dict[str, str] = {}
    rule_definition = rule_definition.replace(" ", "")
    if "//" in rule_definition:
        exception = rule_definition.split("//")[1]
        rule_parts["exception_left"] = exception.split("_")[0]
        rule_parts["exception_right"] = exception.split("_")[1]
        rule_definition = rule_definition.split("//")[0]
    if "/" in rule_definition:
        context = rule_definition.split("/")[1]
        rule_parts["context_left"] = context.split("_")[0]
        rule_parts["context_right"] = context.split("_")[1]
        rule_definition = rule_definition.split("/")[0]
    if "->" in rule_definition:
        rule_parts["target"] = rule_definition.split("->")[0]
        rule_parts["result"] = rule_definition.split("->")[1]
    elif "→" in rule_definition:
        rule_parts["target"] = rule_definition.split("→")[0]
        rule_parts["result"] = rule_definition.split("→")[1]
    return rule_parts


def parse_rule_part(rule_part_string: str):
    """Parse a rule part into a list of Element objects.

    An example rule part: [+cons,-syll]p[]{2,3}
    """
    ...
