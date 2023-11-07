
user_dict = {
    'JuzhanXu': '''Juzhan Xu''',
    'MingLunGong': '''<a href="http://socs.uoguelph.ca/~minglun/">Minglun Gong</a>''',
    'HaoZhang': '''<a href="http://www.cs.sfu.ca/~haoz/">Hao Zhang</a>''',
    'HuiHuang': '''<a href="http://vcc.szu.edu.cn/~huihuang/">Hui Huang</a>''',
    'RuizhenHu': '''<a href="https://csse.szu.edu.cn/staff/ruizhenhu/index.htm">Ruizhen Hu</a>''',
    'ZeyuHuang': '''<a href="https://zzilch.github.io/">Zeyu Huang</a>''',
    'BinChen': '''<a href="#">Bin Chen</a>''',
    'LuanMinChen': '''<a href="#">Luanmin Chen</a>''',
    "OliverVanKaick": '''<a href="http://people.scs.carleton.ca/~olivervankaick/index.html">Oliver van Kaick</a>''',
    "OliverDeussen": '''<a href="https://www.cgmi.uni-konstanz.de/">Oliver Deussen</a>''',
    "ChuanWang": '''<a href="#">Chuan Wang</a>''',
    "HaibinHuang": '''<a href="https://brotherhuang.github.io/">Haibin Huang</a>''',
    "QiJinShe": '''<a href="#">Qijin She</a>''',
    "MinLiu": '''<a href="#">Min Liu</a>''',
    "SisiDai": '''<a href="#">Sisi Dai</a>''',
    "KaiXu": '''<a href="http://kevinkaixu.net/">Kai Xu</a>''',
}

title = "NIFT: Neural Interaction Field and Template for Object Manipulation"

person = [
    'ZeyuHuang',
    'JuzhanXu',
    'SisiDai',
    'KaiXu',
    'HaoZhang',
    'HuiHuang',
    'RuizhenHu',
]
org = 'IEEE International Conference on Robotics and Automation (ICRA), 2023.'

description = "We introduce NIFT, Neural Interaction Field and Template, a descriptive and robust interaction representation of object manipulations to facilitate imitation learning. Given a few object manipulation demos, NIFT guides the generation of the interaction imitation for a new object instance by matching the Neural Interaction Template (NIT) extracted from the demos to the Neural Interaction Field (NIF) defined for the new object."

img = "./assets/nift/img.png"

person_num = len(person)
person_string = ""
for i in range(person_num - 1):
    if i == person_num - 2:
        person_string += user_dict[ person[i] ] + ' and \n'
    else:
        person_string += user_dict[ person[i] ] + ', \n'

person_string += user_dict[ person[person_num-1] ]


tmp = f'''

<img align='right' height='170' src="{img}" alt="图片" />

#### [{title}](#)

{person_string}

{org}
<p>{description}</p>
<br/>

'''

print(tmp)