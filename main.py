#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import jinja2
import webapp2
from models import Film

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)

class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        seznam = Film.query().fetch()
        params = {"seznam": seznam}
        return self.render_template("base.html", params=params)


class VnosHandler(BaseHandler):
    def get(self):
        return self.render_template("vnos.html")

    def post(self):
        name = self.request.get("name")
        year = int(self.request.get("year"))
        genre = self.request.get("genre")
        rating = int(self.request.get("rating"))
        image = self.request.get("image")

        film = Film(name=name, year=year, genre=genre, rating=rating, image=image)
        film.put()
        return self.redirect_to("prva")


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/', MainHandler, name="prva"),
    webapp2.Route('/vnos', VnosHandler),
], debug=True)
