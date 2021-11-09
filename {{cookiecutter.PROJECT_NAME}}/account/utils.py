def jwt_response_payload_handler(token, user, request):
    """
    自定义 jwt 回调函数
    :param token: jwt 生成的 token
    :param user: 登录用户
    :param request: 请求体
    :return:
    """
    if user.is_superuser:
        current_authority = 'admin'
    else:
        current_authority = 'user'

    return {
        'token': token,
        'currentAuthority': current_authority,
        'status': 'ok'
    }
