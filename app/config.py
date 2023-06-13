from datetime import timedelta

class Config:
    # SQLALCHEMY_DATABASE_URI='mysql://root:root@localhost/db_shop_g20'
    SQLALCHEMY_DATABASE_URI='postgresql://db_shop_g20_x0ww_user:B4lGqC05EmJJZX8hOmq0Mb6FYeqOQSVm@dpg-ci3s3g2ip7vptq3s6h40-a.ohio-postgres.render.com/db_shop_g20_x0ww'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    JWT_SECRET_KEY='asdfhasdfhlkasdfl32h'
    JWT_ACCESS_TOKEN_EXPIRES=timedelta(hours=1)