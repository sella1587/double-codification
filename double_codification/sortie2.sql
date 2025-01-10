BEGIN;
--
-- Alter field avec_carlingage on consolidatedobjects
--
ALTER TABLE "j35"."consolidated_objects" ALTER COLUMN "avec_carlingage" TYPE varchar(4) USING "avec_carlingage"::varchar(4);
--
-- Alter field avec_plots on consolidatedobjects
--
ALTER TABLE "j35"."consolidated_objects" ALTER COLUMN "avec_plots" TYPE varchar(4) USING "avec_plots"::varchar(4);
--
-- Alter field degre_choc on consolidatedobjects
--
ALTER TABLE "j35"."consolidated_objects" ALTER COLUMN "degre_choc" TYPE varchar(4) USING "degre_choc"::varchar(4);
--
-- Alter field facteur_choc on consolidatedobjects
--
ALTER TABLE "j35"."consolidated_objects" ALTER COLUMN "facteur_choc" TYPE varchar(4) USING "facteur_choc"::varchar(4);
--
-- Alter field avec_carlingage on objectsfromcao
--
ALTER TABLE "j35"."objects_from_cao" ALTER COLUMN "avec_carlingage" TYPE varchar(4) USING "avec_carlingage"::varchar(4);
--
-- Alter field avec_plots on objectsfromcao
--
ALTER TABLE "j35"."objects_from_cao" RENAME COLUMN "avec_plot" TO "avec_plots";
ALTER TABLE "j35"."objects_from_cao" ALTER COLUMN "avec_plots" TYPE varchar(4) USING "avec_plots"::varchar(4);
--
-- Alter field degre_choc on objectsfromcao
--
ALTER TABLE "j35"."objects_from_cao" ALTER COLUMN "degre_choc" TYPE varchar(4) USING "degre_choc"::varchar(4);
--
-- Alter field facteur_choc on objectsfromcao
--
ALTER TABLE "j35"."objects_from_cao" ALTER COLUMN "facteur_choc" TYPE varchar(4) USING "facteur_choc"::varchar(4);
COMMIT;
