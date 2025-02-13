def typeBasedTransformer(**kwargs):
    update={}
    for name, value in kwargs.items():
        if type(value)==int or type(value)==float:
            update[name]=value*value
        elif type(value) == str:
            update[name]=value[::-1]
        elif type(value) == bool:
            update[name]=not value
        elif type(value) == list or type(value)==tuple:
            update[name]=value[::-1]
        elif type(value) == dict:
            swapped={}
            for x, y in value.items():
                swapped[y]=x
            update[name]=swapped
        else:
            update[name]=value
    return update            

