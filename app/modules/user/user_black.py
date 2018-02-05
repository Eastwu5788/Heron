from flask import g
from . import user

from app.modules.base.base_handler import BaseHandler
from app.modules.vendor.pre_request.flask import filter_params
from app.modules.vendor.pre_request.filter_rules import Rule, Length

from app.models.account.aha_account import AhaAccountModel
from app.models.account.user_black import UserBlackModel
from app.models.account.user_info import UserInfoModel
from app.models.social.image import ImageModel

from app.helper.response import *
from app.helper.auth import login_required
from app.helper.utils import array_column


class IndexHandler(BaseHandler):

    per_page = 20

    rule = {
        "limit": Rule(direct_type=int, allow_empty=True, default=1)
    }

    @login_required
    @filter_params(get=rule)
    def get(self, params):
        offset = IndexHandler.per_page * params["limit"]
        user_black_list = UserBlackModel.query_user_black_list(g.account["user_id"], 1, offset, IndexHandler.per_page)

        user_id_list = array_column(user_black_list, "black_user_id")

        result = list()

        for user_id in user_id_list:

            user_info = UserInfoModel.query_user_model_by_id(user_id)
            if not user_info:
                continue
            item = dict()
            item["user_id"] = user_info.user_id
            item["nickname"] = user_info.nickname

            img = ImageModel.query_image_by_id(user.avatar)
            item["avatar"] = ImageModel.generate_image_url(img, size='b')
            item["huanxin_uid"] = ""
            result.append(item)

        return json_success_response(result)


user.add_url_rule("/getuserblack/index", view_func=IndexHandler.as_view("get_user_black_index"))