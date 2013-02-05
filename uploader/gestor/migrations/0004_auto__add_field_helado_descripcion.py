# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Helado.descripcion'
        db.add_column('gestor_helado', 'descripcion',
                      self.gf('django.db.models.fields.TextField')(default='', max_length=300, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Helado.descripcion'
        db.delete_column('gestor_helado', 'descripcion')


    models = {
        'gestor.helado': {
            'Meta': {'object_name': 'Helado'},
            'descripcion': ('django.db.models.fields.TextField', [], {'max_length': '300', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'sabor': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['gestor']