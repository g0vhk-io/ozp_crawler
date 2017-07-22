# -*- coding: utf-8 -*-
import scrapy
import json

class OzpSpider(scrapy.Spider):
    name = 'ozp'
    start_urls = ['http://www1.ozp.tpb.gov.hk/gos/default.aspx']

    def start_requests(self):
        for u in self.start_urls:
            yield scrapy.Request(u, callback=self.parse)

    def parse(self, response):
        #yield scrapy.Request('http://www1.ozp.tpb.gov.hk/gos/proxy.ashx?http://www1.ozp.tpb.gov.hk/arcgis/rest/services/OBJ_REP/MapServer?f=json&dpi=96&transparent=true&format=png8', callback=self.parse_ozp)   
        for i in range(0, 60):
            start = i * 200
            end = (i + 1) * 200 - 1
            yield scrapy.Request('http://www1.ozp.tpb.gov.hk/gos/proxy.ashx?http://www1.ozp.tpb.gov.hk/arcgis/rest/services/OZP_PLAN/MapServer/0/query?f=json&where=OBJECTID%3E%3D%20' + str(start) + '%20AND%20OBJECTID%20%3C%3D%20' + str(end)+ '&returnGeometry=true&spatialRel=esriSpatialRelIntersects&outFields=*', callback=self.parse_ozp)   

    def parse_ozp(self, response):
        print(response.text)
        
        d = json.loads(response.text)
        features = d["features"]
        if len(features) > 0:
            yield d
