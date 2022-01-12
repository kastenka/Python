# Что запишется в параметры obj и obj_type?
class Descriptor:
  def __get__(self, obj, obj_type):
    pass


class Class:
  attr = Descriptor()


new_obj = Class()
print(new_obj.attr)

# Ответ: В obj - new_obj, в obj_type - Class