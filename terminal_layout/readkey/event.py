class KeyPressEvent(object):
    def __init__(self, k, t):
        """
        
        :param k:
        :type k: KeyInfo
        :param t:
        :type t:
        """
        self.key = k
        self.time = t

    def __str__(self):
        return 'KeyPressEvent(key=<%s>, time=%s)' % (self.key.name, self.time)
