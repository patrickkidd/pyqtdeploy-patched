# Copyright (c) 2022, Riverbank Computing Limited
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.


from abc import abstractmethod

from .component import Component


class AbstractSIPComponent(Component):
    """ The abstract base class for an implementation of a SIP component
    plugin.
    """

    ###########################################################################
    # The following make up the public API to be used by component plugins.
    ###########################################################################

    def __init__(self, *args, **kwargs):
        """ Initialise the component. """

        import warnings

        warnings.warn(
                "AbstractSIPComponent is deprecated, use Component instead",
                DeprecationWarning, stacklevel=2)

        super().__init__(*args, **kwargs)

    @property
    @abstractmethod
    def host_sip(self):
        """ The name of the host sip executable.  This must only be called when
        SIP v4 is being used.
        """

    @property
    @abstractmethod
    def target_sip_dir(self):
        """ The name of the directory containing the target .sip files.  This
        must only be called when SIP v4 is being used.
        """
