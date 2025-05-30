class Vahed:
    def __init__(self, code_dars, name, tedad_vahed, barname, ostad):
        self.code_dars = code_dars
        self.name = name
        self.tedad_vahed = tedad_vahed
        self.barname = barname
        self.ostad = ostad
        
class Student:
    def __init__(self, name, shomare_daneshjo):
        self.name = name
        self.shomare_daneshjo = shomare_daneshjo
        self.selected_vahedha = []
        self.total_units = 0
        
    def add_vahed(self, vahed, hame_vahedha):
        if self.check_barname(vahed):
            self.selected_vahedha.append(vahed)
            self.total_units += vahed.tedad_vahed
            print(vahed.name + ' ' +'انتخاب شد')
        else:
            print('error')
            
    def check_barname(self, vahed):
        for selected_vahed in self.selected_vahedha:
            if vahed.barname == selected_vahed.barname:
                print('error')
                return False
        return True
    
vahedha = [
    Vahed('101' , 'برنامه نویسی پیشرفته 2' , 3 , 'شنبه 8-10' , 'استاد محمود زاده'),
    Vahed('102' , 'گسسته' , 3 , 'شنبه 10-12' , 'استاد قالیشویان'),
    Vahed('103' , 'مدار منطقی' , 3 , 'یکشنبه 8-10' , 'استاد یوسفی'),
    Vahed('104' , 'ریاضی کاربردی' , 2 , 'یکشنبه 10-12' , 'استاد داوود نژاد'),
    Vahed('105' , 'تربیت بدنی' , 1 , 'دوشنبه 8-10' , 'استاد امیری'),
    Vahed('106' , 'برنامه نویسی پیشرفته 1' , 3 , 'شنبه 8-10' , 'استاد ستوده'), 
    Vahed('107' , 'زبان انگلیسی' , 2 , 'سه‌شنبه 8-10' , 'استاد موسوی'),
    Vahed('108' , 'شبکه' , 3 , 'سه‌شنبه 10-12' , 'استاد حسینی'),
    Vahed('109' , 'ورزش' , 1 , 'دوشنبه 8-10' , 'استاد امینی'), ]

name = input('نام دانشجو')
shomare_daneshjo = input('شماره دانشجویی')
student = Student(name, shomare_daneshjo)

print('لیست واحد ها')
for vahed in vahedha:
    print(vahed.code_dars + '    ' + vahed.name + '    ' + vahed.ostad + '    '  + str(vahed.tedad_vahed) )

while student.total_units < 14:
    try:
        choice = input()
        vahed = next((v for v in vahedha if v.code_dars == choice), None)
        if vahed:
            if student.total_units + vahed.tedad_vahed <= 14:
                student.add_vahed(vahed, vahedha)
            else:
                print('error')
        else:
            print('error')
    except ValueError:
        print('erroe')

print('برنامه اين ترم')
for vahed in student.selected_vahedha:
    print(vahed.code_dars + '  ' + vahed.name + '  ' + vahed.ostad + '  ' + str(vahed.tedad_vahed))
