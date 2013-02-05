# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Helado'
        db.create_table('gestor_helado', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('sabor', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('imagen', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('gestor', ['Helado'])


    def backwards(self, orm):
        # Deleting model 'Helado'
        db.delete_table('gestor_helado')


    models = {
        'gestor.helado': {
            'Meta': {'object_name': 'Helado'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'sabor': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['gestor']