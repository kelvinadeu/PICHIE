import unittest
from app import create_app,db
from app.models import User,Role,Comment,Subscribe
from flask_script import Manager,Server
from  flask_migrate import Migrate, MigrateCommand

 #Creating app instance
app = create_app('production')

migrate = Migrate(app,db)
manager = Manager(app)
manager.add_command('db',MigrateCommand)
manager.add_command('Server',Server)

@manager.command
def test():
    """
    Run the unittests.
    """
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User )
if __name__ == '__main__':
    manager.run()
