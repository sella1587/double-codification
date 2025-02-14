BEGIN;
--
-- Create model AvecCarlingage
--
CREATE TABLE "projet"."avec_carlingage" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "avec_carlingage" varchar(75) NOT NULL);
--
-- Create model AvecPlot
--
CREATE TABLE "projet"."avec_plots" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "avec_plots" varchar(150) NOT NULL UNIQUE);
--
-- Create model ConsolidationRule
--
CREATE TABLE "consolidation_rule" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "property_name" varchar(255) NOT NULL, "sources_priorities" text NULL, "display_mode" varchar(50) NOT NULL);
--
-- Create model DegreChoc
--
CREATE TABLE "projet"."degre_choc" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "degre_choc" varchar(50) NOT NULL);
--
-- Create model FacteurChoc
--
CREATE TABLE "projet"."facteur_choc" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "facteur_choc" varchar(5) NOT NULL UNIQUE);
--
-- Create model Ouvrage
--
CREATE TABLE "ouvrage" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "ouvrage" varchar(25) NOT NULL UNIQUE, "type" varchar(50) NOT NULL, "code_client" varchar(150) NOT NULL);
--
-- Create model OwnerCodeDetails
--
CREATE TABLE "j35"."owner_code_details" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "objconso_id" integer NOT NULL, "fieldorder" integer NOT NULL UNIQUE, "fieldvalue" varchar(50) NOT NULL);
--
-- Create model OwnerCodeProperties
--
CREATE TABLE "j35"."owner_code_properties" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "fieledorder" integer NOT NULL UNIQUE, "fieldtype" integer NOT NULL, "fieldvalue" varchar(50) NOT NULL, "fieldlabel" varchar(50) NOT NULL);
--
-- Create model ProprieteDc
--
CREATE TABLE "projet"."proriete_dc" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "property" varchar(50) NOT NULL, "sourcespriorities" varchar(250) NOT NULL, "displaymode" varchar(50) NOT NULL);
--
-- Create model ConsolidatedObjects
--
CREATE TABLE "j35"."consolidated_objects" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "uid" varchar(75) NOT NULL, "source" varchar(150) NOT NULL, "name" varchar(255) NOT NULL, "component_type" varchar(75) NOT NULL, "description" text NOT NULL, "trade" varchar(100) NOT NULL, "function" varchar(50) NOT NULL, "lot" varchar(50) NOT NULL, "room" varchar(50) NOT NULL, "code_client_ouvrage" varchar(75) NOT NULL, "code_client_object" varchar(50) NOT NULL, "code_fournisseur" varchar(50) NOT NULL, "creation_date" timestamp with time zone NOT NULL, "date_last_modified" timestamp with time zone NOT NULL, "archived_date" timestamp with time zone NOT NULL, "avec_carlingage" bigint NOT NULL, "avec_plot" bigint NOT NULL, "degre_choc" bigint NOT NULL, "facteur_choc" bigint NOT NULL);
--
-- Create model ObjectsFromCao
--
CREATE TABLE "j35"."objects_from_cao" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "uid" varchar(75) NOT NULL, "source" varchar(150) NOT NULL, "name" varchar(255) NOT NULL, "component_type" varchar(75) NOT NULL, "description" text NOT NULL, "trade" varchar(100) NOT NULL, "function" varchar(50) NOT NULL, "lot" varchar(50) NOT NULL, "room" varchar(50) NOT NULL, "code_client_ouvrage" varchar(75) NOT NULL, "code_client_object" varchar(50) NOT NULL, "code_fournisseur" varchar(50) NOT NULL, "creation_date" timestamp with time zone NOT NULL, "date_last_modified" timestamp with time zone NOT NULL, "archived_date" timestamp with time zone NOT NULL, "avec_carlingage" bigint NOT NULL, "avec_plot" bigint NOT NULL, "degre_choc" bigint NOT NULL, "facteur_choc" bigint NOT NULL);
CREATE INDEX "avec_plots_avec_plots_e48d8633_like" ON "projet"."avec_plots" ("avec_plots" varchar_pattern_ops);
CREATE INDEX "facteur_choc_facteur_choc_8e114128_like" ON "projet"."facteur_choc" ("facteur_choc" varchar_pattern_ops);
CREATE INDEX "ouvrage_ouvrage_f12574d5_like" ON "ouvrage" ("ouvrage" varchar_pattern_ops);
CREATE INDEX "consolidated_objects_avec_carlingage_7f371b76" ON "j35"."consolidated_objects" ("avec_carlingage");
CREATE INDEX "consolidated_objects_avec_plot_814553c5" ON "j35"."consolidated_objects" ("avec_plot");
CREATE INDEX "consolidated_objects_degre_choc_2f47ef3b" ON "j35"."consolidated_objects" ("degre_choc");
CREATE INDEX "consolidated_objects_facteur_choc_b0e5fb95" ON "j35"."consolidated_objects" ("facteur_choc");
CREATE INDEX "objects_from_cao_avec_carlingage_065b8477" ON "j35"."objects_from_cao" ("avec_carlingage");
CREATE INDEX "objects_from_cao_avec_plot_f4e1d513" ON "j35"."objects_from_cao" ("avec_plot");
CREATE INDEX "objects_from_cao_degre_choc_7c68920e" ON "j35"."objects_from_cao" ("degre_choc");
CREATE INDEX "objects_from_cao_facteur_choc_cf9d1148" ON "j35"."objects_from_cao" ("facteur_choc");
COMMIT;
