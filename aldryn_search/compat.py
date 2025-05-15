import cms

from looseversion import LooseVersion


GTE_CMS_35 = LooseVersion(cms.__version__) >= LooseVersion('3.5')
GTE_CMS_50 = LooseVersion(cms.__version__) >= LooseVersion('5.0')


def is_authenticated(user):
    try:
        return user.is_authenticated()  # Django<1.10
    except TypeError:
        return user.is_authenticated  # Django>=1.10
