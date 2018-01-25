"""
定义所有错误的code与描述
"""

error_message = {
    501: "请求方式错误",
    502: "请求参数验证失败",
    503: "授权认证失败",
    504: "",

    2002: "数据异常",
    2017: "密码长度只能6位",
    2018: "密码只能使用字母或数字",

    2101: "用户为空",
    2102: "登录异常",
    2103: "退出失败",
    2105: "您的账号已存在",
    2106: "您的账号因违规已被封禁！",

    2201: "不可以发纯文本动态哦~",

    5010: "验证码用完了，请明天再来吧。",
    5011: "用户不存在，请检查您的手机号",
    5012: "验证码发送失败",

    5100: "昵称不能为空",
    5101: "该昵称已被占用",

    10001: "验证码错误",
}