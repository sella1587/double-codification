BEGIN;
--
-- Alter field archived_date on consolidatedobjects
--
ALTER TABLE "j35"."consolidated_objects" ALTER COLUMN "archived_date" DROP NOT NULL;
--
-- Alter field avec_plots on consolidatedobjects
--
ALTER TABLE "j35"."consolidated_objects" ALTER COLUMN "avec_plots" DROP NOT NULL;
--
-- Alter field code_client_object on consolidatedobjects
--
ALTER TABLE "j35"."consolidated_objects" ALTER COLUMN "code_client_object" DROP NOT NULL;
--
-- Alter field code_client_ouvrage on consolidatedobjects
--
ALTER TABLE "j35"."consolidated_objects" ALTER COLUMN "code_client_ouvrage" DROP NOT NULL;
--
-- Alter field code_fournisseur on consolidatedobjects
--
ALTER TABLE "j35"."consolidated_objects" ALTER COLUMN "code_fournisseur" DROP NOT NULL;
--
-- Alter field component_type on consolidatedobjects
--
ALTER TABLE "j35"."consolidated_objects" ALTER COLUMN "component_type" DROP NOT NULL;
--
-- Alter field creation_date on consolidatedobjects
--
ALTER TABLE "j35"."consolidated_objects" ALTER COLUMN "creation_date" DROP NOT NULL;
--
-- Alter field date_last_modified on consolidatedobjects
--
ALTER TABLE "j35"."consolidated_objects" ALTER COLUMN "date_last_modified" DROP NOT NULL;
--
-- Alter field degre_choc on consolidatedobjects
--
ALTER TABLE "j35"."consolidated_objects" ALTER COLUMN "degre_choc" DROP NOT NULL;
--
-- Alter field description on consolidatedobjects
--
ALTER TABLE "j35"."consolidated_objects" ALTER COLUMN "description" DROP NOT NULL;
--
-- Alter field facteur_choc on consolidatedobjects
--
ALTER TABLE "j35"."consolidated_objects" ALTER COLUMN "facteur_choc" DROP NOT NULL;
--
-- Alter field function on consolidatedobjects
--
ALTER TABLE "j35"."consolidated_objects" ALTER COLUMN "function" DROP NOT NULL;
--
-- Alter field lot on consolidatedobjects
--
ALTER TABLE "j35"."consolidated_objects" ALTER COLUMN "lot" DROP NOT NULL;
--
-- Alter field room on consolidatedobjects
--
ALTER TABLE "j35"."consolidated_objects" ALTER COLUMN "room" DROP NOT NULL;
--
-- Alter field trade on consolidatedobjects
--
ALTER TABLE "j35"."consolidated_objects" ALTER COLUMN "trade" DROP NOT NULL;
--
-- Alter field archived_date on objectsfromcao
--
ALTER TABLE "j35"."objects_from_cao" ALTER COLUMN "archived_date" DROP NOT NULL;
--
-- Alter field avec_carlingage on objectsfromcao
--
ALTER TABLE "j35"."objects_from_cao" ALTER COLUMN "avec_carlingage" DROP NOT NULL;
--
-- Alter field avec_plots on objectsfromcao
--
ALTER TABLE "j35"."objects_from_cao" ALTER COLUMN "avec_plots" DROP NOT NULL;
--
-- Alter field code_client_object on objectsfromcao
--
ALTER TABLE "j35"."objects_from_cao" ALTER COLUMN "code_client_object" DROP NOT NULL;
--
-- Alter field code_client_ouvrage on objectsfromcao
--
ALTER TABLE "j35"."objects_from_cao" ALTER COLUMN "code_client_ouvrage" DROP NOT NULL;
--
-- Alter field code_fournisseur on objectsfromcao
--
ALTER TABLE "j35"."objects_from_cao" ALTER COLUMN "code_fournisseur" DROP NOT NULL;
--
-- Alter field component_type on objectsfromcao
--
ALTER TABLE "j35"."objects_from_cao" ALTER COLUMN "component_type" DROP NOT NULL;
--
-- Alter field date_last_modified on objectsfromcao
--
ALTER TABLE "j35"."objects_from_cao" ALTER COLUMN "date_last_modified" DROP NOT NULL;
--
-- Alter field degre_choc on objectsfromcao
--
ALTER TABLE "j35"."objects_from_cao" ALTER COLUMN "degre_choc" DROP NOT NULL;
--
-- Alter field description on objectsfromcao
--
ALTER TABLE "j35"."objects_from_cao" ALTER COLUMN "description" DROP NOT NULL;
--
-- Alter field facteur_choc on objectsfromcao
--
ALTER TABLE "j35"."objects_from_cao" ALTER COLUMN "facteur_choc" DROP NOT NULL;
--
-- Alter field function on objectsfromcao
--
ALTER TABLE "j35"."objects_from_cao" ALTER COLUMN "function" DROP NOT NULL;
--
-- Alter field lot on objectsfromcao
--
ALTER TABLE "j35"."objects_from_cao" ALTER COLUMN "lot" DROP NOT NULL;
--
-- Alter field room on objectsfromcao
--
ALTER TABLE "j35"."objects_from_cao" ALTER COLUMN "room" DROP NOT NULL;
--
-- Alter field trade on objectsfromcao
--
ALTER TABLE "j35"."objects_from_cao" ALTER COLUMN "trade" DROP NOT NULL;
COMMIT;
