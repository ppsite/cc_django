import hashlib
import random


class IDAvatar(object):
    """
    ID Avatar Generator
    mm： 简约、卡通风格的人物轮廓像（不会随邮箱哈希值变化而变化）
    identicon：几何图案，其形状会随电子邮箱哈希值变化而变化
    monsterid：程序生成的“怪兽”头像，颜色和面孔会随会随电子邮箱哈希值变化而变化
    wavatar:：用不同面容和背景组合生成的面孔头像
    retro：程序生成的8位街机像素头像
    """
    url = 'http://www.gravatar.com/avatar/'
    size = 80
    dlist = ['mm', 'identicon', 'monsterid', 'wavatar', 'retro']  # 头像类型列表

    def __init__(self, username: str) -> None:
        """
        :param username: 用户名
        """
        self.md5 = hashlib.md5(f'{username}'.encode('utf-8')).hexdigest()

    def generate(self, d: str) -> str:
        """
        生成头像地址
        :param d: 头像类型
        :return: URL
        """
        return '%s%s?s=%d&d=%s' % (self.url, self.md5, self.size, d)

    def mm(self):
        return self.generate(d='mm')

    def identicon(self):
        return self.generate(d='identicon')

    def monsterid(self):
        return self.generate(d='monsterid')

    def wavatar(self):
        return self.generate(d='wavatar')

    def retro(self):
        return self.generate(d='retro')

    def random(self):
        return self.generate(d=random.choices(self.dlist)[0])
