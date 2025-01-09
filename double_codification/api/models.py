from django.db import models

class FacteurChoc(models.Model):
    facteur_choc = models.CharField(max_length=5, unique=True)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now_add=True)
    class Meta:
        db_table = '"projet"."facteur_choc"'

class DegreChoc(models.Model):
    degre_choc  = models.CharField(max_length=50)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now_add=True)
    class Meta:
        db_table = '"projet"."degre_choc"'

class AvecPlot(models.Model):
    avec_plots = models.CharField(max_length=150, unique=True)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now_add=True)
    class Meta:
        db_table = '"projet"."avec_plots"'
class AvecCarlingage(models.Model):
    avec_carlingage = models.CharField(max_length=75)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now_add=True)
    class Meta:
        db_table = '"projet"."avec_carlingage"'

class ProprieteDc(models.Model):
    property = models.CharField(max_length=50)
    sourcespriorities = models.CharField(max_length=250)
    displaymode = models.CharField(max_length=50)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now_add=True)
    class Meta:
        db_table = '"projet"."proriete_dc"'

class Ouvrage(models.Model):
    ouvrage = models.CharField(max_length=25, unique=True)
    type = models.CharField(max_length=50)
    code_client = models.CharField(max_length=150)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now_add=True)
    class Meta:
        db_table = "ouvrage"
    # add validation rules for code_client

class ObjectsFromCao(models.Model):
    uid = models.CharField(max_length=75, null=False)
    source = models.CharField(max_length=150, null=False)
    name = models.CharField(max_length=255, null=False)
    component_type = models.CharField(max_length=75)
    description = models.TextField()
    trade = models.CharField(max_length=100)
    function = models.CharField(max_length=50)
    lot = models.CharField(max_length=50)
    room = models.CharField(max_length=50)
    code_client_ouvrage = models.CharField(max_length=75)
    code_client_object = models.CharField(max_length=50)
    code_fournisseur = models.CharField(max_length=50)
    facteur_choc = models.ForeignKey(FacteurChoc, on_delete=models.DO_NOTHING)
    degre_choc = models.ForeignKey(DegreChoc, on_delete=models.DO_NOTHING)
    avec_plot = models.ForeignKey(AvecPlot, on_delete=models.DO_NOTHING)
    avec_carlingage = models.ForeignKey(AvecCarlingage, on_delete=models.DO_NOTHING)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    archived_date = models.DateTimeField()
    class Meta:
        db_table = '"j35"."objects_from_cao"'

class ConsolidatedObjects(models.Model):
    uid = models.CharField(max_length=75, null=False)
    source = models.CharField(max_length=150, null=False)
    name = models.CharField(max_length=255, null=False)
    component_type = models.CharField(max_length=75)
    description = models.TextField()
    trade = models.CharField(max_length=100)
    function = models.CharField(max_length=50)
    lot = models.CharField(max_length=50)
    room = models.CharField(max_length=50)
    code_client_ouvrage = models.CharField(max_length=75)
    code_client_object = models.CharField(max_length=50)
    code_fournisseur = models.CharField(max_length=50)
    facteur_choc = models.ForeignKey(FacteurChoc, on_delete=models.DO_NOTHING)
    degre_choc = models.ForeignKey(DegreChoc, on_delete=models.DO_NOTHING)
    avec_plot = models.ForeignKey(AvecPlot, on_delete=models.DO_NOTHING)
    avec_carlingage = models.ForeignKey(AvecCarlingage, on_delete=models.DO_NOTHING)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    archived_date = models.DateTimeField()
    class Meta:
        db_table = '"j35"."consolidated_objects"'


class OwnerCodeDetails(models.Model):
    objconso_id  = models.IntegerField(null=False)
    fieldorder = models.IntegerField(null=False, unique=True)    
    fieldvalue = models.CharField(max_length=50)    
    class Meta:
        db_table = '"j35"."owner_code_details"'

class OwnerCodeProperties(models.Model):
    fieledorder = models.IntegerField(null=False, unique=True)
    fieldtype = models.IntegerField(null=False)
    fieldvalue = models.CharField(max_length=50)
    fieldlabel = models.CharField(max_length=50)
    class Meta:
        db_table = '"j35"."owner_code_properties"'
