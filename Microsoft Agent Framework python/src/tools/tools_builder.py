from typing import List, Any


def discover_tools(*tool_instances) -> List[Any]:
    """
    Collect all tools functions from multiple Tools instances.
    
    Args:
        *tool_instances: Variable number of Tools class instances
        
    Returns:
        List of all tool functions from all provided instances
    """
    all_tools = []
    for instance in tool_instances:
        if hasattr(instance, 'get_tools') and callable(getattr(instance, 'get_tools')):
            all_tools.extend(instance.get_tools())
        else:
            # Auto-discover methods with @tool decorator
            for attr_name in dir(instance):
                if attr_name.startswith('_'):
                    continue
                attr = getattr(instance, attr_name)
                if callable(attr):
                    # Check for tool-specific attributes
                    if hasattr(attr, '__wrapped__') or hasattr(attr, 'description'):
                        all_tools.append(attr)
    return all_tools
