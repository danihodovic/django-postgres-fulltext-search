from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        # NOTE: The previous migration probably looks different for you, so
        # modify this.
        ('web', '0002_auto_20190525_0647'),
    ]

    migration = '''
        CREATE TRIGGER content_search_update BEFORE INSERT OR UPDATE
        ON web_page FOR EACH ROW EXECUTE FUNCTION
        tsvector_update_trigger(content_search, 'pg_catalog.english', content);

        -- Force triggers to run and populate the text_search column.
        UPDATE web_page set ID = ID;
    '''

    reverse_migration = '''
        DROP TRIGGER content_search ON web_page;
    '''

    operations = [
        migrations.RunSQL(migration, reverse_migration)
    ]
