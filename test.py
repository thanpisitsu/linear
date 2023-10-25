from bs4 import BeautifulSoup
import js2py

# Your HTML content containing the JavaScript code
html = """
<html>
  <head>
    <script></script>
    <script>
      var GEEK = {};
      GEEK.geekitemPreload = {
        property1: "value1",
        property2: "value2"
      };
    </script>
  </head>
</html>
"""

# Create a BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

# Find the script tag containing JavaScript code
script_tag = soup.findAll('script')

for i in script_tag:
    try :
        javascript_code = i.string

        # Execute the JavaScript code using js2py
        context = js2py.EvalJs()
        context.execute(javascript_code)

        # Access specific properties of the GEEK.geekitemPreload object
        geekitem_preload = context.GEEK.geekitemPreload
        property1 = geekitem_preload.property1
        property2 = geekitem_preload.property2

        # Print the values
        print(property1)
        print(property2)
    except :
        print(1)


