# -*- coding: utf-8 -*-
from flask_restful import Api, Resource


class HealthController(Resource):
    def get(self):
        return {"status": "ok"}
