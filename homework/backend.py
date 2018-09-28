import base64


def get_args(cmd="pwd"):
    ip = "172.19.17.6"
    cmd = base64.b64encode(cmd)
    ip_list = [{"ip": ip, "bk_cloud_id": 0}]
    args = {"bk_biz_id": 2, "script_content": cmd, "account": "root", "ip_list": ip_list}
    return args