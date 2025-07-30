#!/usr/bin/env python3

try:
    from langchain_community.tools import DuckDuckGoSearchRun
    print("✓ DuckDuckGo import successful")
    
    tool = DuckDuckGoSearchRun()
    print("✓ DuckDuckGo tool created successfully")
    
    # Test the tool
    result = tool.run("test search")
    print(f"✓ DuckDuckGo search test successful: {len(result)} characters returned")
    
except ImportError as e:
    print(f"✗ Import error: {e}")
except Exception as e:
    print(f"✗ Error: {e}")