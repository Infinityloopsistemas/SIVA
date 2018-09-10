<?php

if(!isset($_SERVER['HTTP_X_PJAX'])){

    $content = basename($_SERVER['SCRIPT_NAME']);

    $_SERVER['HTTP_X_PJAX'] = true;
    include 'stilearn.base.template.php';
    die();
}

?>
                    <!-- Typography
                    ================================================== -->
                    <div class="row">
                        <div class="col-md-6" data-toggle="sortable-widget">
                            <!-- Headings -->
                            <div id="panel-typohead" class="panel panel-default sortable-widget-item">
                                <div class="panel-heading">
                                    <div class="panel-actions">
                                        <button data-collapse="#panel-typohead" title="collapse" class="btn-panel">
                                            <i class="fa fa-caret-down"></i>
                                        </button>
                                        <button data-close="#panel-typohead" title="close" class="btn-panel">
                                            <i class="fa fa-times"></i>
                                        </button>
                                    </div><!-- /panel-actions -->
                                    <h3 class="panel-title sortable-widget-handle">Headings</h3>
                                </div><!-- /panel-heading -->

                                <div class="panel-body">
                                    <p>All HTML headings, <code>&lt;h1&gt;</code> through <code>&lt;h6&gt;</code>, are available. <code>.h1</code> through <code>.h6</code> classes are also available, for when you want to match the font styling of a heading but still want your text to be displayed inline.</p>
                                    <table class="table demo-table">
                                        <tbody>
                                            <tr class="bordered-bottom">
                                                <td><h1>h1. Bootstrap heading <small>Sub text</small></h1></td>
                                                <td class="text-muted">Semibold 36px</td>
                                            </tr>
                                            <tr class="bordered-bottom">
                                                <td><h2>h2. Bootstrap heading <small>Sub text</small></h2></td>
                                                <td class="text-muted">Semibold 30px</td>
                                            </tr>
                                            <tr class="bordered-bottom">
                                                <td><h3>h3. Bootstrap heading <small>Sub text</small></h3></td>
                                                <td class="text-muted">Semibold 24px</td>
                                            </tr>
                                            <tr class="bordered-bottom">
                                                <td><h4>h4. Bootstrap heading <small>Sub text</small></h4></td>
                                                <td class="text-muted">Semibold 18px</td>
                                            </tr>
                                            <tr class="bordered-bottom">
                                                <td><h5>h5. Bootstrap heading <small>Sub text</small></h5></td>
                                                <td class="text-muted">Semibold 14px</td>
                                            </tr>
                                            <tr>
                                                <td><h6>h6. Bootstrap heading <small>Sub text</small></h6></td>
                                                <td class="text-muted">Semibold 12px</td>
                                            </tr>
                                        </tbody>
                                    </table>
                                    <pre class="no-padding prettyprint">&lt;h1&gt;h1. Bootstrap heading &lt;small&gt;Sub text&lt;/small&gt;&lt;/h1&gt;
&lt;h2&gt;h2. Bootstrap heading &lt;small&gt;Sub text&lt;/small&gt;&lt;/h2&gt;
&lt;h3&gt;h3. Bootstrap heading &lt;small&gt;Sub text&lt;/small&gt;&lt;/h3&gt;
&lt;h4&gt;h4. Bootstrap heading &lt;small&gt;Sub text&lt;/small&gt;&lt;/h4&gt;
&lt;h5&gt;h5. Bootstrap heading &lt;small&gt;Sub text&lt;/small&gt;&lt;/h5&gt;
&lt;h6&gt;h6. Bootstrap heading &lt;small&gt;Sub text&lt;/small&gt;&lt;/h6&gt;</pre>
                                </div><!-- /panel-body -->
                            </div><!-- /panel-typohead -->


                            <!-- Body copy & Lead -->
                            <div id="panel-bodycopy" class="panel panel-default sortable-widget-item">
                                <div class="panel-heading">
                                    <div class="panel-actions">
                                        <button data-collapse="#panel-bodycopy" title="collapse" class="btn-panel">
                                            <i class="fa fa-caret-down"></i>
                                        </button>
                                        <button data-close="#panel-bodycopy" title="close" class="btn-panel">
                                            <i class="fa fa-times"></i>
                                        </button>
                                    </div><!-- /panel-actions -->
                                    <h3 class="panel-title sortable-widget-handle">Body copy & Lead</h3>
                                </div><!-- /panel-heading -->

                                <div class="panel-body">
                                    <p>Bootstrap's global default <code>font-size</code> is <strong class="text-linethrough">14px</strong>, it convert to <strong>13px</strong> on Stilearn Admin, with a <code>line-height</code> of <strong>1.428</strong>. This is applied to the <code>.content</code> and all paragraphs. In addition, <code>&lt;p&gt;</code> (paragraphs) receive a bottom margin of half their computed line-height (10px by default).</p>
                                    <p>Nullam quis risus eget urna mollis ornare vel eu leo. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nullam id dolor id nibh ultricies vehicula.</p>
                                    <p class="lead">Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec ullamcorper nulla non metus auctor fringilla. Duis mollis, est non commodo luctus, nisi erat porttitor ligula, eget lacinia odio sem nec elit. Donec ullamcorper nulla non metus auctor fringilla.</p>
                                    <p>Make a paragraph stand out by adding <code>.lead</code>. Default style with <strong>16px</strong> <code>font-size</code>, <strong>1.4em</strong> <code>line-height</code> and <strong>200</strong> <code>font-weight</code>.</p>
                                    <pre class="no-padding prettyprint">&lt;p&gt;...&lt;p&gt;
&lt;p class=&quot;lead&quot;&gt;...&lt;p&gt;</pre>
                                </div><!-- /panel-body -->
                            </div><!-- /panel-bodycopy -->


                            <!-- Abbreviations -->
                            <div id="panel-abbreviations" class="panel panel-default sortable-widget-item">
                                <div class="panel-heading">
                                    <div class="panel-actions">
                                        <button data-collapse="#panel-abbreviations" title="collapse" class="btn-panel">
                                            <i class="fa fa-caret-down"></i>
                                        </button>
                                        <button data-close="#panel-abbreviations" title="close" class="btn-panel">
                                            <i class="fa fa-times"></i>
                                        </button>
                                    </div><!-- /panel-actions -->
                                    <h3 class="panel-title sortable-widget-handle">Abbreviations & Address</h3>
                                </div><!-- /panel-heading -->

                                <div class="panel-body">
                                    <!-- Abbreviations -->
                                    <p>Stylized implementation of HTML's <code>&lt;abbr&gt;</code> element for abbreviations and acronyms to show the expanded version on hover. Abbreviations with a <code>title</code> attribute have a light dotted bottom border and a help cursor on hover, providing additional context on hover.</p>
                                    <h3>Basic abbreviation</h3>
                                    <p>For expanded text on long hover of an abbreviation, include the <code>title</code> attribute with the <code>&lt;abbr&gt;</code> element.</p>
                                    <p>An abbreviation of the word attribute is <abbr title="attribute">attr</abbr>.</p>

                                    <pre class="no-padding prettyprint">&lt;abbr title=&quot;attribute&quot;&gt;attr&lt;abbr&gt;</pre>
                                    <h3>Initialism</h3>
                                    <p>Add <code>.initialism</code> to an abbreviation for a slightly smaller font-size.</p>
                                    <p><abbr title="HyperText Markup Language" class="initialism">HTML</abbr> is the best thing since sliced bread.</p>
                                    <pre class="no-padding prettyprint">&lt;abbr title=&quot;HyperText Markup Language&quot; class=&quot;initialism&quot;&gt;HTML&lt;abbr&gt;</pre>

                                    <!-- Addresses -->
                                    <h3>Addresses</h3>
                                    <p>Present contact information for the nearest ancestor or the entire body of work. Preserve formatting by ending all lines with <code>&lt;br&gt;</code>.</p>
                                    <div>
                                        <address>
                                            <strong>Twitter, Inc.</strong><br>
                                            795 Folsom Ave, Suite 600<br>
                                            San Francisco, CA 94107<br>
                                            <abbr title="Phone">P:</abbr> (123) 456-7890
                                        </address>
                                        <address>
                                            <strong>Full Name</strong><br>
                                            <a href="mailto:#">first.last@example.com</a>
                                        </address>
                                    </div>
                                    <pre class="no-padding prettyprint">&lt;address&gt;
    &lt;strong&gt;Twitter, Inc.&lt;/strong&gt;&lt;br&gt;
    795 Folsom Ave, Suite 600&lt;br&gt;
    San Francisco, CA 94107&lt;br&gt;
    &lt;abbr title=&quot;Phone&quot;&gt;P:&lt;/abbr&gt; (123) 456-7890
&lt;/address&gt;

&lt;address&gt;
    &lt;strong&gt;Full Name&lt;/strong&gt;&lt;br&gt;
    &lt;a href=&quot;mailto:#&quot;&gt;first.last@example.com&lt;/a&gt;
&lt;/address&gt;</pre>

                                </div><!-- /panel-body -->
                            </div><!-- /panel-abbreviations -->


                            <!-- Code -->
                            <div id="panel-code" class="panel panel-default sortable-widget-item">
                                <div class="panel-heading">
                                    <div class="panel-actions">
                                        <button data-collapse="#panel-code" title="collapse" class="btn-panel">
                                            <i class="fa fa-caret-down"></i>
                                        </button>
                                        <button data-close="#panel-code" title="close" class="btn-panel">
                                            <i class="fa fa-times"></i>
                                        </button>
                                    </div><!-- /panel-actions -->
                                    <h3 class="panel-title sortable-widget-handle">Code</h3>
                                </div><!-- /panel-heading -->

                                <div class="panel-body">
                                    <h3>Inline</h3>
                                    <p>Wrap inline snippets of code with <code>&lt;code&gt;</code>.</p>
                                    <p>For example, <code>&lt;section&gt;</code> should be wrapped as inline.</p>
                                    <pre class="no-padding prettyprint">For example, &lt;code&gt;&amp;lt;section&amp;gt;&lt;/code&gt; should be wrapped as inline.</pre>

                                    <h3>User input</h3>
                                    <p>Use the <code>&lt;kbd&gt;</code> to indicate input that is typically entered via keyboard.</p>
                                    <p>To switch directories, type <kbd>cd</kbd> followed by the name of the directory.</p>
                                    <pre class="no-padding prettyprint">&lt;p&gt;To switch directories, type &lt;kbd&gt;cd&lt;/kbd&gt; followed by the name of the directory.&lt;/p&gt;</pre>

                                    <h3>Basic block</h3>
                                    <p>Use <code>&lt;pre&gt;</code> for multiple lines of code. Be sure to escape any angle brackets in the code for proper rendering.</p>
                                    <pre>&lt;p&gt;Sample text here...&lt;/p&gt;</pre>
                                    <p><em>You may optionally add the</em> <code>.pre-scrollable</code> <em>class, which will set a max-height of 350px and provide a y-axis scrollbar.</em></p>
                                    <p><strong>NOTE: </strong> when you use <code>.pre-scrollable</code>, the Pre Element will automatically use the Nice Scroll. To disable it you can use <code>.nicescroll-off</code>. Please <a data-pjax=".content-body" href="helper-classes.php">see this in Action</a></p>
                                    <pre class="no-padding prettyprint">&lt;pre&gt;&amp;lt;p&amp;gt;Sample text here...&amp;lt;/p&amp;gt;&lt;/pre&gt;</pre>
                                    
                                    <h3>Google code prettify</h3>
                                    <p>User <code>pre</code> width class <code>.prettyprint</code> to enable syntax highlighting of source code snippets in an html page.</p>
                                    <pre class="no-padding prettyprint lang-basic">&lt;script type=&quot;text/javascript&quot;&gt;
// Say hello world until the user starts questioning
// the meaningfulness of their existence.
function helloWorld(world) {
    for (var i = 42; --i >= 0;) {
        alert('Hello ' + String(world));
    }
}
&lt;/script&gt;</pre>
                                </div><!-- /panel-body -->
                            </div><!-- /panel-code -->
                            
                        </div><!--/cols-->



                        <div class="col-md-6" data-toggle="sortable-widget">
                            <!-- Emphasis -->
                            <div id="panel-emphasis" class="panel panel-default sortable-widget-item">
                                <div class="panel-heading">
                                    <div class="panel-actions">
                                        <button data-collapse="#panel-emphasis" title="collapse" class="btn-panel">
                                            <i class="fa fa-caret-down"></i>
                                        </button>
                                        <button data-close="#panel-emphasis" title="close" class="btn-panel">
                                            <i class="fa fa-times"></i>
                                        </button>
                                    </div><!-- /panel-actions -->
                                    <h3 class="panel-title sortable-widget-handle">Emphasis</h3>
                                </div><!-- /panel-heading -->

                                <div class="panel-body">
                                    <!-- Emphasis -->
                                    <p>Make use of HTML's default emphasis tags with lightweight styles.</p>
                                    <h3>Small text</h3>
                                    <p>For de-emphasizing inline or blocks of text, use the <code>&lt;small&gt;</code> tag to set text at 80% the size of the parent. Heading elements receive their own <code>font-size</code> for nested <code>&lt;small&gt;</code> elements.</p>
                                    <p>You may alternatively use an inline element with <code>.small</code> in place of any <code>&lt;small&gt;</code></p>
                                    <p><small>This line of text is meant to be treated as fine print.</small></p>
                                    <pre class="no-padding prettyprint">&lt;small&gt;This line of text is meant to be treated as fine print.&lt;/small&gt;</pre>

                                    <h3>Bold</h3>
                                    <p>For emphasizing a snippet of text with a heavier font-weight.</p>
                                    <p>The following snippet of text is <strong>rendered as bold text</strong>.</p>
                                    <pre class="no-padding prettyprint">&lt;strong&gt;rendered as bold text&lt;/strong&gt;</pre>

                                    <h3>Italics</h3>
                                    <p>For emphasizing a snippet of text with italics.</p>
                                    <p>The following snippet of text is <em>rendered as italicized text</em>.</p>
                                    <pre class="no-padding prettyprint">&lt;em&gt;rendered as italicized text&lt;/em&gt;</pre>

                                    <div class="callout callout-info">
                                        <h4>Alternate elements</h4>
                                        <p>Feel free to use <code>&lt;b&gt;</code> and <code>&lt;i&gt;</code> in HTML5. <code>&lt;b&gt;</code> is meant to highlight words or phrases without conveying additional importance while <code>&lt;i&gt;</code> is mostly for voice, technical terms, etc.</p>
                                    </div>

                                    <h3>Alignment classes</h3>
                                    <p>Easily realign text to components with text alignment classes.</p>
                                    <div>
                                        <p class="text-left">Left aligned text.</p>
                                        <p class="text-center">Center aligned text.</p>
                                        <p class="text-right">Right aligned text.</p>
                                    </div>
                                    <pre class="no-padding prettyprint">&lt;p class=&quot;text-left&quot;&gt;Left aligned text.&lt;/p&gt;
&lt;p class=&quot;text-center&quot;&gt;Center aligned text.&lt;/p&gt;
&lt;p class=&quot;text-right&quot;&gt;Right aligned text.&lt;/p&gt;</pre>
                                    <h3>Emphasis classes</h3>
                                    <p>Convey meaning through color with a handful of emphasis utility classes. These may also be applied to links and will darken on hover just like our default link styles.</p>
                                    <div>
                                        <p class="text-muted">Fusce dapibus, tellus ac cursus commodo, tortor mauris nibh.</p>
                                        <p class="text-primary">Nullam id dolor id nibh ultricies vehicula ut id elit.</p>
                                        <p class="text-success">Duis mollis, est non commodo luctus, nisi erat porttitor ligula.</p>
                                        <p class="text-info">Maecenas sed diam eget risus varius blandit sit amet non magna.</p>
                                        <p class="text-warning">Etiam porta sem malesuada magna mollis euismod.</p>
                                        <p class="text-danger">Donec ullamcorper nulla non metus auctor fringilla.</p>
                                    </div>
                                    <pre class="no-padding prettyprint">&lt;p class=&quot;text-muted&quot;&gt;...&lt;/p&gt;
&lt;p class=&quot;text-primary&quot;&gt;...&lt;/p&gt;
&lt;p class=&quot;text-success&quot;&gt;...&lt;/p&gt;
&lt;p class=&quot;text-info&quot;&gt;...&lt;/p&gt;
&lt;p class=&quot;text-warning&quot;&gt;...&lt;/p&gt;
&lt;p class=&quot;text-danger&quot;&gt;...&lt;/p&gt;</pre>

                                    <div class="callout callout-info callout-right">
                                        <h4>Dealing with specificity</h4>
                                        <p>Sometimes emphasis classes cannot be applied due to the specificity of another selector. In most cases, a sufficient workaround is to wrap your text in a <code>&lt;span&gt;</code> with the class.</p>
                                    </div>
                                </div><!-- /panel-body -->
                            </div><!-- /panel-emphasis -->


                            <!-- Blockquotes -->
                            <div id="panel-blockquote" class="panel panel-default sortable-widget-item">
                                <div class="panel-heading">
                                    <div class="panel-actions">
                                        <button data-collapse="#panel-blockquote" title="collapse" class="btn-panel">
                                            <i class="fa fa-caret-down"></i>
                                        </button>
                                        <button data-close="#panel-blockquote" title="close" class="btn-panel">
                                            <i class="fa fa-times"></i>
                                        </button>
                                    </div><!-- /panel-actions -->
                                    <h3 class="panel-title sortable-widget-handle">Blockquotes</h3>
                                </div><!-- /panel-heading -->

                                <div class="panel-body">
                                    <p>For quoting blocks of content from another source within your document.</p>
                                    <h3>Default blockquote</h3>
                                    <p>Wrap <code>&lt;blockquote&gt;</code> around any <abbr title="HyperText Markup Language">HTML</abbr> as the quote. For straight quotes, we recommend a <code>&lt;p&gt;</code>.</p>
                                    <blockquote>
                                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.</p>
                                    </blockquote>
                                    <pre class="no-padding prettyprint">&lt;blockquote&gt;
    &lt;p&gt;Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.&lt;/p&gt;
&lt;/blockquote&gt;</pre>
                                    
                                    <h3>Blockquote options</h3>
                                    <p>Style and content changes for simple variations on a standard <code>&lt;blockquote&gt;</code>.</p>

                                    <h4>Naming a source</h4>
                                    <p>Add <code>&lt;small&gt;</code> tag or <code>.small</code> class for identifying the source. Wrap the name of the source work in <code>&lt;cite&gt;</code>.</p>

                                    <blockquote>
                                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.</p>
                                        <small>Someone famous in <cite title="Source Title">Source Title</cite></small>
                                    </blockquote>
                                    <pre class="no-padding prettyprint">&lt;blockquote&gt;
    &lt;p&gt;Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.&lt;/p&gt;
    &lt;small&gt;Someone famous in &lt;cite title=&quot;Source Title&quot;&gt;Source Title&lt;/cite&gt;&lt;/small&gt;
&lt;/blockquote&gt;</pre>
                                    
                                    <h4>Alternate displays</h4>
                                    <p>Use <code>.pull-right</code> for a floated, right-aligned blockquote.</p>
                                    <div class="clearfix">
                                        <blockquote class="pull-right">
                                            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.</p>
                                            <small>Someone famous in <cite title="Source Title">Source Title</cite></small>
                                        </blockquote>
                                    </div>
                                    <pre class="no-padding prettyprint">&lt;blockquote class=&quot;pull-right&quot;&gt;
    ...
&lt;/blockquote&gt;</pre>
                                </div><!-- /panel-body -->
                            </div><!-- /panel-blockquote -->

                        </div><!--/cols-->
                    </div><!--/row-->



                    <!-- Lists -->
                    <div class="row">
                        <div class="col-md-12">
                            <!-- Lists -->
                            <div id="panel-lists" class="panel panel-default sortable-widget-item">
                                <div class="panel-heading">
                                    <div class="panel-actions">
                                        <button data-collapse="#panel-lists" title="collapse" class="btn-panel">
                                            <i class="fa fa-caret-down"></i>
                                        </button>
                                        <button data-close="#panel-lists" title="close" class="btn-panel">
                                            <i class="fa fa-times"></i>
                                        </button>
                                    </div><!-- /panel-actions -->
                                    <h3 class="panel-title sortable-widget-handle">Lists</h3>
                                </div><!-- /panel-heading -->

                                <div class="panel-body">
                                    <div class="row">
                                        <div class="col-md-4">
                                            <h3>Unordered</h3>
                                            <p>A list of items in which the order does <em>not</em> explicitly matter.</p>
                                            <ul>
                                                <li>Lorem ipsum dolor sit amet</li>
                                                <li>Consectetur adipiscing elit</li>
                                                <li>Integer molestie lorem at massa</li>
                                                <li>Facilisis in pretium nisl aliquet</li>
                                                <li>Nulla volutpat aliquam velit
                                                    <ul>
                                                        <li>Phasellus iaculis neque</li>
                                                        <li>Purus sodales ultricies</li>
                                                        <li>Vestibulum laoreet porttitor sem</li>
                                                        <li>Ac tristique libero volutpat at</li>
                                                    </ul>
                                                </li>
                                                <li>Faucibus porta lacus fringilla vel</li>
                                                <li>Aenean sit amet erat nunc</li>
                                                <li>Eget porttitor lorem</li>
                                            </ul>
                                            <pre class="prettyprint">&lt;ul&gt;
  &lt;li&gt;...&lt;/li&gt;
&lt;/ul&gt;</pre>
                                        </div><!--/cols-->

                                        <div class="col-md-4">
                                            <h3>Ordered</h3>
                                            <p>A list of items in which the order <em>does</em> explicitly matter.</p>
                                            <ol>
                                                <li>Lorem ipsum dolor sit amet</li>
                                                <li>Consectetur adipiscing elit</li>
                                                <li>Integer molestie lorem at massa</li>
                                                <li>Facilisis in pretium nisl aliquet</li>
                                                <li>Nulla volutpat aliquam velit
                                                    <ol>
                                                        <li>Phasellus iaculis neque</li>
                                                        <li>Purus sodales ultricies</li>
                                                        <li>Vestibulum laoreet porttitor sem</li>
                                                        <li>Ac tristique libero volutpat at</li>
                                                    </ol>
                                                </li>
                                                <li>Faucibus porta lacus fringilla vel</li>
                                                <li>Aenean sit amet erat nunc</li>
                                                <li>Eget porttitor lorem</li>
                                            </ol>
                                            <pre class="prettyprint">&lt;ol&gt;
  &lt;li&gt;...&lt;/li&gt;
&lt;/ol&gt;</pre>
                                        </div><!--/cols-->

                                        <div class="col-md-4">
                                            <h3>Unstyled</h3>
                                            <p>Remove the default <code>list-style</code> and left margin on list items (immediate children only). <strong>This only applies to immediate children list items</strong>, meaning you will need to add the class for any nested lists as well.</p>
                                            <ul class="list-unstyled">
                                                <li>Lorem ipsum dolor sit amet</li>
                                                <li>Consectetur adipiscing elit</li>
                                                <li>Nulla volutpat aliquam velit
                                                    <ul>
                                                        <li>Phasellus iaculis neque</li>
                                                        <li>Purus sodales ultricies</li>
                                                        <li>Vestibulum laoreet porttitor sem</li>
                                                    </ul>
                                                </li>
                                                <li>Faucibus porta lacus fringilla vel</li>
                                                <li>Aenean sit amet erat nunc</li>
                                                <li>Eget porttitor lorem</li>
                                            </ul>
                                            <pre class="prettyprint">&lt;ul class=&quot;list-unstyled&quot;&gt;
  &lt;li&gt;...&lt;/li&gt;
&lt;/ul&gt;</pre>
                                        </div><!--/cols-->

                                        <div class="col-md-12">
                                            <h3>Inline</h3>
                                            <p>Place all list items on a single line with <code>display: inline-block;</code> and some light padding.</p>
                                            <ul class="list-inline" rel="tooltip" title="I'm a block of Inline List">
                                                <li>Lorem ipsum</li>
                                                <li>Phasellus iaculis</li>
                                                <li>Nulla volutpat</li>
                                                <li>Nulla</li>
                                                <li>volutpat</li>
                                                <li>aliquam</li>
                                                <li>velit</li>
                                            </ul>
                                            <pre class="prettyprint">&lt;ul class=&quot;list-inline&quot;&gt;
  &lt;li&gt;...&lt;/li&gt;
&lt;/ul&gt;</pre>
                                        </div><!--/cols-->

                                        <div class="col-md-4">
                                            <h3>List Icons</h3>
                                            <p>Use <code>fa-ul</code> and <code>fa-li</code> to easily replace default bullets in unordered lists. Can use with all of <a rel="tooltip" title="Font Awesome" target="_blank" href="http://fortawesome.github.io/Font-Awesome/icons/">Icons Font Awesome</a></p>
                                            <ul class="fa-ul">
                                                <li><i class="fa-li fa fa-check-square"></i>List icons (like these)</li>
                                                <li><i class="fa-li fa fa-check-square"></i>can be used</li>
                                                <li><i class="fa-li fa fa-spinner fa-spin"></i>to replace</li>
                                                <li><i class="fa-li fa fa-square"></i>default bullets in lists</li>
                                                <li><i class="fa-li fa fa-angle-right"></i>angle stye</li>
                                                <li><i class="fa-li fa fa-angle-double-right"></i>double angle</li>
                                                <li><i class="fa-li fa fa-caret-right"></i>or caret</li>
                                                <li><i class="fa-li fa fa-compress"></i>something else</li>
                                            </ul>
                                            <pre class="prettyprint">&lt;ul class=&quot;fa-ul&quot;&gt;
  &lt;li&gt;&lt;i class=&quot;fa-li fa fa-check-square&quot;&gt;&lt;/i&gt; List icons&lt;/li&gt;
&lt;/ul&gt;</pre>
                                        </div><!--/cols-->
                                        <div class="col-md-4">
                                            <h3>Description</h3>
                                            <p style="margin-bottom:19px;">A list of terms with their associated descriptions.</p>
                                            <dl>
                                                <dt>Description lists</dt>
                                                <dd>A description list is perfect for defining terms.</dd>
                                                <dt>Euismod</dt>
                                                <dd>Vestibulum id ligula porta felis euismod semper eget lacinia odio sem nec elit.</dd>
                                                <dd>Donec id elit non mi porta gravida at eget metus.</dd>
                                                <dt>Malesuada porta</dt>
                                                <dd>Etiam porta sem malesuada magna mollis euismod.</dd>
                                            </dl>
                                            <pre class="prettyprint" style="margin-top:5px">&lt;dl&gt;
    &lt;dt&gt;...&lt;/dt&gt;
    &lt;dd&gt;...&lt;/dd&gt;
&lt;/dl&gt;</pre>
                                        </div><!--/cols-->
                                        <div class="col-md-4">
                                            <h4>Horizontal description</h4>
                                            <p style="margin-bottom:15px;">Make terms and descriptions in <code>&lt;dl&gt;</code> line up side-by-side. Starts off stacked like default <code>&lt;dl&gt;</code>s, but when the navbar expands, so do these.</p>
                                            <dl class="dl-horizontal">
                                                <dt>Malesuada porta</dt>
                                                <dd>Etiam porta sem malesuada magna mollis euismod.</dd>
                                                <dt>Felis euismod semper eget lacinia</dt>
                                                <dd>Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus.</dd>
                                            </dl>
                                            <pre class="prettyprint">&lt;dl class=&quot;dl-horizontal&quot;&gt;
    &lt;dt&gt;...&lt;/dt&gt;
    &lt;dd&gt;...&lt;/dd&gt;
&lt;/dl&gt;</pre>
                                        </div><!--/cols-->
                                    </div><!--/row-->
                                </div><!-- /panel-body -->
                            </div><!-- /panel-lists -->
                        </div><!--/cols-->
                    </div><!--/row-->