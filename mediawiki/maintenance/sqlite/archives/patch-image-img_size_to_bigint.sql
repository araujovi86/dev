-- This file is automatically generated using maintenance/generateSchemaChangeSql.php.
-- Source: abstractSchemaChanges/patch-image-img_size_to_bigint.json
-- Do not modify this file directly.
-- See https://www.mediawiki.org/wiki/Manual:Schema_changes
CREATE TEMPORARY TABLE /*_*/__temp__image AS
SELECT  img_name,  img_size,  img_width,  img_height,  img_metadata,  img_bits,  img_media_type,  img_major_mime,  img_minor_mime,  img_description_id,  img_actor,  img_timestamp,  img_sha1
FROM  /*_*/image;
DROP  TABLE  /*_*/image;
CREATE TABLE  /*_*/image (    img_name BLOB DEFAULT '' NOT NULL,    img_size BIGINT UNSIGNED DEFAULT 0 NOT NULL,    img_width INTEGER DEFAULT 0 NOT NULL,    img_height INTEGER DEFAULT 0 NOT NULL,    img_metadata BLOB NOT NULL,    img_bits INTEGER DEFAULT 0 NOT NULL,    img_media_type TEXT DEFAULT NULL,    img_major_mime TEXT DEFAULT 'unknown' NOT NULL,    img_minor_mime BLOB DEFAULT 'unknown' NOT NULL,    img_description_id BIGINT UNSIGNED NOT NULL,    img_actor BIGINT UNSIGNED NOT NULL,    img_timestamp BLOB NOT NULL,    img_sha1 BLOB DEFAULT '' NOT NULL,    PRIMARY KEY(img_name)  );
INSERT INTO  /*_*/image (    img_name, img_size, img_width, img_height,    img_metadata, img_bits, img_media_type,    img_major_mime, img_minor_mime,    img_description_id, img_actor, img_timestamp,    img_sha1  )
SELECT  img_name,  img_size,  img_width,  img_height,  img_metadata,  img_bits,  img_media_type,  img_major_mime,  img_minor_mime,  img_description_id,  img_actor,  img_timestamp,  img_sha1
FROM  /*_*/__temp__image;
DROP  TABLE /*_*/__temp__image;
CREATE INDEX img_actor_timestamp ON  /*_*/image (img_actor, img_timestamp);
CREATE INDEX img_size ON  /*_*/image (img_size);
CREATE INDEX img_timestamp ON  /*_*/image (img_timestamp);
CREATE INDEX img_sha1 ON  /*_*/image (img_sha1);
CREATE INDEX img_media_mime ON  /*_*/image (    img_media_type, img_major_mime, img_minor_mime  );