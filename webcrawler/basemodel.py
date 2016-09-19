#coding:utf-8
'''
@Author: Xiaozhe Yaoi <i@askfermi.me>
'''
import leancloud

class Field(object):

    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

class StringField(Field):

    def __init__(self, name):
        super(StringField, self).__init__(name, 'string')

class ModelMetaClass(type):
    def __new__(cls,name,bases,attrs):
        if __name__=='Model':
            return type.__new__(cls,name,bases,attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v,Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k]=v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings
        attrs['__table__'] = name
        return type.__new__(cls, name, bases, attrs)

class Model(dict):
    __metaclass__ = ModelMetaClass
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    '''
    Overwrite this method to support Database etc.
    '''
    def save(self):
        LeanObj=leancloud.Object.extend(self.__table__)
        lo=LeanObj()
        for k, v in self.__mappings__.items():
            lo.set(k,self[k])
        try:
            lo.save()
        except Exception,e:
            print 'Save to Leancloud Failed.'
            print str(e)
            raise ValueError('Save to Leancloud Failed.')

