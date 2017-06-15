# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-03 08:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nas_name', models.CharField(db_column='nasname', db_index=True, help_text='NAS Name (or IP address)', max_length=128, unique=True, verbose_name='nas name')),
                ('short_name', models.CharField(db_column='shortname', max_length=32, verbose_name='short name')),
                ('type', models.CharField(db_column='type', max_length=30, verbose_name='type')),
                ('secret', models.CharField(db_column='secret', help_text='Shared Secret', max_length=60, verbose_name='secret')),
                ('ports', models.IntegerField(blank=True, db_column='ports', null=True, verbose_name='ports')),
                ('community', models.CharField(blank=True, db_column='community', max_length=50, null=True, verbose_name='community')),
                ('description', models.CharField(db_column='description', max_length=200, null=True, verbose_name='description')),
                ('server', models.CharField(db_column='server', max_length=64, null=True, verbose_name='server')),
            ],
            options={
                'verbose_name': 'nas',
                'db_table': 'nas',
                'verbose_name_plural': 'nas',
            },
        ),
        migrations.CreateModel(
            name='RadiusAccounting',
            fields=[
                ('rad_acct_id', models.BigIntegerField(db_column='radacctid', primary_key=True, serialize=False)),
                ('acct_session_id', models.CharField(db_column='acctsessionid', db_index=True, max_length=64)),
                ('acct_unique_id', models.CharField(db_column='acctuniqueid', max_length=32, unique=True)),
                ('user_name', models.CharField(db_column='username', db_index=True, max_length=64, verbose_name='username')),
                ('group_name', models.CharField(db_column='groupname', max_length=64, verbose_name='groupname')),
                ('realm', models.CharField(db_column='realm', max_length=64, null=True, verbose_name='realm')),
                ('nas_ip_address', models.CharField(db_column='nasipaddress', db_index=True, max_length=15)),
                ('nas_port_id', models.CharField(db_column='nasportid', max_length=15, null=True)),
                ('nas_port_type', models.CharField(db_column='nasporttype', max_length=32, verbose_name='nas port type')),
                ('acct_start_time', models.DateTimeField(db_column='acctstarttime', db_index=True, verbose_name='acct start time')),
                ('acct_stop_time', models.DateTimeField(db_column='acctstoptime', db_index=True, null=True, verbose_name='acct stop time')),
                ('acct_session_time', models.IntegerField(db_column='acctsessiontime', db_index=True, null=True, verbose_name='acct session time')),
                ('acct_authentic', models.CharField(db_column='acctauthentic', max_length=32, null=True, verbose_name='acct authentic')),
                ('connection_info_start', models.CharField(db_column='connectinfo_start', max_length=50, null=True, verbose_name='connection info start')),
                ('connection_info_stop', models.CharField(db_column='connectinfo_stop', max_length=50, null=True, verbose_name='connection info stop')),
                ('acct_input_octets', models.BigIntegerField(db_column='acctinputoctets', null=True, verbose_name='acct input octets')),
                ('acct_output_octets', models.BigIntegerField(db_column='acctoutputoctets', null=True, verbose_name='acct output octets')),
                ('callingStationId', models.CharField(db_column='calledstationid', max_length=50)),
                ('calledStationId', models.CharField(db_column='callingstationid', max_length=50)),
                ('acct_terminate_cause', models.CharField(db_column='acctterminatecause', max_length=32, verbose_name='acct terminate cause')),
                ('service_type', models.CharField(db_column='servicetype', max_length=32, null=True, verbose_name='service type')),
                ('framed_protocol', models.CharField(db_column='framedprotocol', max_length=32, null=True, verbose_name='framed protocol')),
                ('framed_ip_address', models.CharField(db_column='framedipaddress', db_index=True, max_length=15)),
                ('acct_start_delay', models.IntegerField(db_column='acctstartdelay', null=True, verbose_name='acct start delay')),
                ('acct_stop_delay', models.IntegerField(db_column='acctstopdelay', null=True, verbose_name='acct stop delay')),
                ('xascend_session_svrkey', models.CharField(db_column='xascendsessionsvrkey', max_length=10, null=True, verbose_name='xascend session svrkey')),
            ],
            options={
                'verbose_name': 'accounting',
                'db_table': 'radacct',
                'verbose_name_plural': 'accounting',
            },
        ),
        migrations.CreateModel(
            name='RadiusCheck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(db_column='username', db_index=True, max_length=64, verbose_name='username')),
                ('value', models.CharField(db_column='value', default='==', max_length=253, verbose_name='radiusvalue')),
                ('op', models.CharField(db_column='op', max_length=2, verbose_name='operator')),
                ('attribute', models.CharField(db_column='attribute', max_length=64, verbose_name='attribute')),
            ],
            options={
                'verbose_name': 'radiuscheck',
                'db_table': 'radcheck',
                'verbose_name_plural': 'radiuschecks',
            },
        ),
        migrations.CreateModel(
            name='RadiusGroup',
            fields=[
                ('id', models.UUIDField(db_column='id', primary_key=True, serialize=False)),
                ('group_name', models.CharField(db_column='username', db_index=True, max_length=255, unique=True, verbose_name='groupname')),
                ('priority', models.IntegerField(db_column='priority', default=1, verbose_name='priority')),
                ('creation_date', models.DateField(db_column='created_at', null=True, verbose_name='creation date')),
                ('modification_date', models.DateField(db_column='updated_at', null=True, verbose_name='modification date')),
                ('notes', models.CharField(blank=True, db_column='notes', max_length=64, null=True, verbose_name='notes')),
            ],
            options={
                'verbose_name': 'radiusgroup',
                'db_table': 'radiusgroup',
                'verbose_name_plural': 'radiusgroups',
            },
        ),
        migrations.CreateModel(
            name='RadiusGroupCheck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(db_column='groupname', db_index=True, max_length=64, verbose_name='groupname')),
                ('attribute', models.CharField(db_column='attribute', max_length=64, verbose_name='attribute')),
                ('op', models.CharField(choices=[('=', '='), (':=', ':='), ('==', '=='), ('+=', '+='), ('!=', '!='), ('>', '>'), ('>=', '>='), ('<', '<'), ('<=', '<='), ('=~', '=~'), ('!~', '!~'), ('=*', '=*'), ('!*', '!*')], db_column='op', default='==', max_length=2, verbose_name='operator')),
                ('value', models.CharField(db_column='value', max_length=253, verbose_name='value')),
            ],
            options={
                'verbose_name': 'radiusgroupcheck',
                'db_table': 'radgroupcheck',
                'verbose_name_plural': 'radiusgroupcheck',
            },
        ),
        migrations.CreateModel(
            name='RadiusGroupReply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(db_column='groupname', db_index=True, max_length=64, verbose_name='groupname')),
                ('attribute', models.CharField(db_column='attribute', max_length=64, verbose_name='attribute')),
                ('op', models.CharField(choices=[('=', '='), (':=', ':='), ('+=', '+=')], db_column='op', default='=', max_length=2, verbose_name='operator')),
                ('value', models.CharField(db_column='value', max_length=253, verbose_name='value')),
            ],
            options={
                'verbose_name': 'radiusgroupreply',
                'db_table': 'radgroupreply',
                'verbose_name_plural': 'radiusgroupreplies',
            },
        ),
        migrations.CreateModel(
            name='RadiusGroupUsers',
            fields=[
                ('user_name', models.CharField(db_column='username', max_length=64, unique=True, verbose_name='username')),
                ('id', models.UUIDField(db_column='id', primary_key=True, serialize=False)),
                ('group_name', models.CharField(db_column='groupname', max_length=255, unique=True, verbose_name='groupname')),
                ('radius_check', models.ManyToManyField(blank=True, db_column='radiuscheck', to='django_freeradius.RadiusCheck', verbose_name='radius check')),
            ],
            options={
                'verbose_name': 'radiusgroupusers',
                'db_table': 'radiusgroupusers',
                'verbose_name_plural': 'radiusgroupusers',
            },
        ),
        migrations.CreateModel(
            name='RadiusPostAuthentication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(db_column='username', max_length=64, verbose_name='username')),
                ('password', models.CharField(db_column='pass', max_length=64, verbose_name='password')),
                ('reply', models.CharField(db_column='reply', max_length=32, verbose_name='reply')),
                ('auth_date', models.DateTimeField(auto_now=True, db_column='authdate', verbose_name='authdate')),
            ],
            options={
                'verbose_name': 'radiuspostauthentication',
                'db_table': 'radpostauth',
                'verbose_name_plural': 'radiuspostauthentication',
            },
        ),
        migrations.CreateModel(
            name='RadiusReply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(db_column='username', db_index=True, max_length=64, verbose_name='username')),
                ('value', models.CharField(db_column='value', max_length=253, verbose_name='value')),
                ('op', models.CharField(db_column='op', default='=', max_length=2, verbose_name='operator')),
                ('attribute', models.CharField(db_column='attribute', max_length=64, verbose_name='attribute')),
            ],
            options={
                'verbose_name': 'radiusreply',
                'db_table': 'radreply',
                'verbose_name_plural': 'radiusreplies',
            },
        ),
        migrations.CreateModel(
            name='RadiusUserGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(db_column='username', db_index=True, max_length=64, verbose_name='username')),
                ('group_name', models.CharField(db_column='groupname', max_length=64, verbose_name='groupname')),
                ('priority', models.IntegerField(db_column='priority', default=1, verbose_name='priority')),
            ],
            options={
                'verbose_name': 'radiususergroup',
                'db_table': 'radusergroup',
                'verbose_name_plural': 'radiususergroup',
            },
        ),
        migrations.AddField(
            model_name='radiusgroupusers',
            name='radius_reply',
            field=models.ManyToManyField(blank=True, db_column='radiusreply', to='django_freeradius.RadiusReply', verbose_name='radius reply'),
        ),
    ]