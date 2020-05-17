class Items:
    """Creates general class to contain miscelaneous items"""
    def __init__(self):
        self.name = "" # name of item
        self.description = "" # description of item
        self.price = 0 # assumed in gold piece
        self.weight = 0

    ## THE FOLLOWING IS A DANGEROUS METHOD AND THUS HAS A PRIVATE ACCESSOR
    ##  HOW TO USE:
    ##    Say you initialize an item as my_item (i.e. my_item = Items())
    ##    instead of accessing this method as my_item.__set_attr(x, y),
    ##    you MUST write it as my_item._Items__set_attr(x, y), otherwise you
    ##    will get an error saying the method does not exist.
    def __set_attr(self, attr_name, attr_value):
        """
        Takes a string attr_name, and any value you'd like for attr_value.

        Sets a new custom attribute for the instance of this object:
        i.e. <variable_name>.<attr_name> = <attr_value>
        """
        setattr(self, attr_name, attr_value)
