
#في لغة Python، هناك ثلاثة أنواع من الدوال المرتبطة بالـ class: class methods و static methods و instance methods.

#1. Class Methods:


#   - تعرف باستخدام الديكوريتور @classmethod.
#   - تستخدم للتعامل مع الـ class نفسه بشكل عام، بدلاً من الـ instance.
 #  - يتم تمرير الـ class كمعامل أولي إلى الـ class method.
 #  - يمكن استخدامها لإنشاء أو تعديل أو حذف متغيرات الـ class، وأيضًا لإنشاء أو تعديل أو حذف دوال الـ class.
   
class MyClass:
    class_variable = "Class Variable"

    @classmethod
    def class_method(cls):
        print("This is a class method")
        print("Class variable:", cls.class_variable)


# استدعاء الـ class method بدون إنشاء instance
MyClass.class_method()






print("############################################")



#2.Instance Methods:
  # - هي الدوال التي يتم تعريفها داخل الـ class وتستخدم self كمعامل أولي.
 #  - يمكن الوصول إليها فقط عبر الـ instance من الـ class.
  # - تستخدم للتعامل مع الـ instance نفسها، والتعامل مع متغيرات الـ instance وتعديلها.



class MyClass:
    class_variable = "Class Variable"

    def instance_method(self):
        print("This is an instance method")
        print("Class variable:", self.class_variable)

# إنشاء كائن من الكلاس
my_object = MyClass()

# استدعاء الـ instance method على الكائن
my_object.instance_method()

print("############################################")


##3. Static Methods:
  #  تعرف باستخدام الديكوريتور @staticmethod# 
 #  لا تستخدم self أو cls كمعاملات.#
 #  - لا تتأثر بالـ instance أو الـ class.#
 #  - تستخدم لإنشاء دوال مستقلة عن الـ instance والـ class والتي يمكن استخدامها بشكل مباشر من الـ class نفسها.#
   
 

class MyClass:
    class_variable = "Class Variable"

    @staticmethod
    def static_method():
        print("This is a static method")
        print("Class variable:", MyClass.class_variable)

# استدعاء الـ static method مباشرة على الكلاس
MyClass.static_method()

