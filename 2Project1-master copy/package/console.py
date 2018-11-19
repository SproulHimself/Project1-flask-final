# from package.data_builder import *
# import os.remove, errno
#
# engine = create_engine('sqlite:///EPL_fantasy.db')
#
#
# def db_creator(filename):
#     try:
#         os.remove(filename)
#     except OSError as e:
#         if e.errno != errno.ENOENT: # errno.ENOENT = no such file or directory
#             raise
#         else:
#             Base.metadata.create_all(engine)
#
#
# db_creator('/Users/sproul/Downloads/Project12-master/EPL_fantasy.db')
#
# Session = sessionmaker(bind=engine)
# session = Session()
#
# session.add_all(team_results)
# session.commit()
