#!/usr/bin/env python

# Author: Felix Wiemann
# Contact: Felix_Wiemann@ososo.de
# Revision: $Revision$
# Date: $Date$
# Copyright: This module has been placed in the public domain.

"""
Test for docutils XML writer.
"""

import unittest

import docutils
import docutils.core


class DocutilsXMLTestCase(unittest.TestCase, docutils.SettingsSpec):

    input = 'Test\n====\n\nSubsection\n----------\n\nTest\n\n----------\n\nTest.'
    xmldecl = '<?xml version="1.0" encoding="iso-8859-1"?>\n'
    doctypedecl = '<!DOCTYPE document PUBLIC "+//IDN docutils.sourceforge.net//DTD Docutils Generic//EN//XML" "http://docutils.sourceforge.net/docs/ref/docutils.dtd">\n'
    generatedby = '<!-- Generated by Docutils %s -->\n' % docutils.__version__
    bodynormal = '<document ids="test" names="test" source="&lt;string&gt;"><title>Test</title><subtitle ids="subsection" names="subsection">Subsection</subtitle><paragraph>Test</paragraph><transition/><paragraph>Test.</paragraph></document>'
    bodynormal = '<document ids="test" names="test" source="&lt;string&gt;"><title>Test</title><subtitle ids="subsection" names="subsection">Subsection</subtitle><paragraph>Test</paragraph><transition/><paragraph>Test.</paragraph></document>'
    bodynewlines = '<document ids="test" names="test" source="&lt;string&gt;">\n<title>\nTest\n</title>\n<subtitle ids="subsection" names="subsection">\nSubsection\n</subtitle>\n<paragraph>\nTest\n</paragraph>\n<transition/>\n<paragraph>\nTest.\n</paragraph>\n</document>\n'
    bodyindents = '<document ids="test" names="test" source="&lt;string&gt;">\n    <title>\n        Test\n    </title>\n    <subtitle ids="subsection" names="subsection">\n        Subsection\n    </subtitle>\n    <paragraph>\n        Test\n    </paragraph>\n    <transition/>\n    <paragraph>\n        Test.\n    </paragraph>\n</document>\n'

    settings_default_overrides = {'_disable_config': 1}

    def test_publish(self):
        settings = {'output_encoding': 'iso-8859-1'}
        for settings['newlines'] in 0, 1:
            for settings['indents'] in 0, 1:
                for settings['xml_declaration'] in 0, 1:
                    for settings['doctype_declaration'] in 0, 1:

                        expected = ''
                        if settings['xml_declaration']:
                            expected += self.xmldecl
                        if settings['doctype_declaration']:
                            expected += self.doctypedecl
                        expected += self.generatedby
                        if settings['indents']:
                            expected += self.bodyindents
                        elif settings['newlines']:
                            expected += self.bodynewlines
                        else:
                            expected += self.bodynormal

                        self.assertEqual(docutils.core.publish_string
                                         (source=self.input,
                                          reader_name='standalone',
                                          writer_name='docutils_xml',
                                          settings_spec=self,
                                          settings_overrides=settings),
                                         expected)


if __name__ == '__main__':
    unittest.main()
