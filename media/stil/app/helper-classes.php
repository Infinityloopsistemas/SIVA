<?php

if(!isset($_SERVER['HTTP_X_PJAX'])){

    $content = basename($_SERVER['SCRIPT_NAME']);

    $_SERVER['HTTP_X_PJAX'] = true;
    include 'stilearn.base.template.php';
    die();
}

?>
                    <!-- HELPER CLASS
                    ================================================== -->
                    <!-- HELPER CLASS & RESPONSIVE UTILITIES  -->
                    <div id="panel-helpclass" class="panel panel-default">
                        <div class="panel-heading">
                            <div class="panel-actions">
                                <button data-refresh="#panel-helpclass" title="refresh" class="btn-panel">
                                    <i class="fa fa-refresh"></i>
                                </button>
                                <button data-expand="#panel-helpclass" title="expand" class="btn-panel">
                                    <i class="fa fa-expand"></i>
                                </button>
                                <button data-collapse="#panel-helpclass" title="collapse" class="btn-panel">
                                    <i class="fa fa-caret-down"></i>
                                </button>
                                <button data-close="#panel-helpclass" title="close" class="btn-panel">
                                    <i class="fa fa-times"></i>
                                </button>
                            </div><!-- /panel-actions -->
                            <h3 class="panel-title">Helper Classes</h3>
                        </div><!-- /panel-heading -->

                        <div class="panel-body">
                            <div class="row">
                                <div class="col-md-6">
                                    <p class="text-muted"><strong>Close icon</strong></p>
                                    <p>Use the generic close icon for dismissing content like modals and alerts.</p>
                                    <p><button type="button" class="close" aria-hidden="true" style="float:none">&times;</button></p>
                                    <pre class="prettyprint">&lt;button type=&quot;button&quot; class=&quot;close&quot; aria-hidden=&quot;true&quot;&gt;&amp;times;&lt;/button&gt;</pre>
                                    <br>
                                    
                                    <p class="text-muted" id="helper-classes-floats"><strong>Quick floats</strong></p>
                                    <p>Float an element to the left or right with a class. <code>!important</code> is included to avoid specificity issues. Classes can also be used as mixins.</p>
                                    <pre class="prettyprint">&lt;div class=&quot;pull-left&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;pull-right&quot;&gt;...&lt;/div&gt;</pre>
                                    <br>

                                    <p class="text-muted"><strong>Clearfix</strong></p>
                                    <p>Clear the <code>float</code> on any element with the <code>.clearfix</code> class. Utilizes <a target="_blank" href="http://nicolasgallagher.com/micro-clearfix-hack/">the micro clearfix</a> as popularized by Nicolas Gallagher. Can also be used as a mixin.</p>
                                    <pre class="prettyprint">&lt;!-- Usage as a class --&gt;
&lt;div class=&quot;clearfix&quot;&gt;...&lt;/div&gt;</pre>
                                    <br>

                                    <p class="text-muted"><strong>Screen reader content</strong></p>
                                    <p>Hide an element to all devices <strong>except screen readers</strong> with <code>.sr-only</code>. Necessary for following <a target="_blank" href="http://getbootstrap.com/getting-started/#accessibility">Bootstrap accessibility best practices</a>.</p>
                                    <pre class="prettyprint">&lt;a class=&quot;sr-only&quot; href=&quot;#content&quot;&gt;Skip to main content&lt;/a&gt;</pre>
                                    <br>

                                    <p class="text-muted"><strong>Background helper</strong></p>
                                    <p>Allows you to select the background as you want, use with <code>!important</code>. This also changed the font color.</p>
                                    <p>
                                        <span class="demo-box bg-midnight">.bg-midnight</span>
                                        <span class="demo-box bg-cloud">.bg-cloud</span>
                                        <span class="demo-box bg-silver">.bg-silver</span>
                                        <span class="demo-box bg-white bordered">.bg-white</span>
                                        <span class="demo-box bg-darknight">.bg-darknight</span>

                                        <span class="demo-box bg-primary">.bg-primary</span>
                                        <span class="demo-box bg-success">.bg-success</span>
                                        <span class="demo-box bg-info">.bg-info</span>
                                        <span class="demo-box bg-warning">.bg-warning</span>
                                        <span class="demo-box bg-danger">.bg-danger</span>
                                    </p>

                                    <pre class="prettyprint">&lt;div class=&quot;bg-primary&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;bg-success&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;bg-info&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;bg-warning&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;bg-danger&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;bg-inverse&quot;&gt;...&lt;/div&gt;

&lt;!-- Also avilable --&gt;
&lt;div class=&quot;bg-darknight&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;bg-midnight&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;bg-cloud&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;bg-silver&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;bg-white&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;bg-teal&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;bg-green&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;bg-orange&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;bg-red&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;bg-blue&quot;&gt;...&lt;/div&gt;</pre>
                                    <br>

                                    <p class="text-muted"><strong>Border Helper</strong></p>
                                    <p>Add class <code>.bordered</code> to give a border on any element. Default style <code>1px solid #E0E4E8</code>. See demo and available class below:</p>
                                    <p>
                                        <span class="demo-box bordered">.bordered</span>
                                        <span class="demo-box bordered-flat">.bordered-flat</span>
                                        <span class="demo-box bordered-top">.bordered-top</span>
                                        <span class="demo-box bordered-right bordered-left" title="bordered right and left">.bordered right left</span>
                                        <span class="demo-box bordered-bottom">.bordered-bottom</span>

                                        <span class="demo-box bordered-flat border-primary">.border-primary</span>
                                        <span class="demo-box bordered-flat border-green">.border-green</span>
                                        <span class="demo-box bordered-flat border-info">.border-info</span>
                                        <span class="demo-box bordered-flat border-orange">.border-orange</span>
                                        <span class="demo-box bordered-flat border-midnight">.border-midnight</span>
                                    </p>
                                    <pre class="prettyprint pre-scrollable nicescroll-off">&lt;div class=&quot;bordered&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;bordered-top&quot;&gt;...&lt;/div&gt; &lt;!-- bordered on top only --&gt;
&lt;div class=&quot;bordered-right&quot;&gt;...&lt;/div&gt; &lt;!-- bordered on right only --&gt;
&lt;div class=&quot;bordered-bottom&quot;&gt;...&lt;/div&gt; &lt;!-- bordered on bottom only --&gt;
&lt;div class=&quot;bordered-left&quot;&gt;...&lt;/div&gt; &lt;!-- bordered on top left --&gt;
&lt;div class=&quot;bordered-flat&quot;&gt;...&lt;/div&gt; &lt;!-- bordered all, but 2px on bottom --&gt;

&lt;!-- Also can change border color --&gt;
&lt;div class=&quot;border-primary&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;border-success&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;border-info&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;border-warning&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;border-danger&quot;&gt;...&lt;/div&gt;

&lt;div class=&quot;border-darknight&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;border-midnight&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;border-cloud&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;border-silver&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;border-white&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;border-teal&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;border-green&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;border-orange&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;border-red&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;border-blue&quot;&gt;...&lt;/div&gt;

&lt;!-- Disable border --&gt;
&lt;div class=&quot;no-border&quot;&gt;...&lt;/div&gt;</pre>
                                    <p><i class="fa fa-hand-o-up"></i> <small>use <code>.pre-scrollable .nicescroll-off</code></small></p>
                                </div><!--/cols -->

                                <div class="col-md-6">
                                    <p class="text-muted"><strong>Carets</strong></p>
                                    <p>Use carets to indicate dropdown functionality and direction. Note that the default caret will reverse automatically in <a href="buttons.php">dropup menus</a>.</p>
                                    <p><span class="caret"></span></p>
                                    <pre class="prettyprint">&lt;span class=&quot;caret&quot;&gt;&lt;/span&gt;</pre>
                                    <br>

                                    <p class="text-muted"><strong>Center content blocks</strong></p>
                                    <p>Set an element to <code>display: block</code> and center via <code>margin</code>. Available as a mixin and class.</p>
                                    <pre class="prettyprint">&lt;div class=&quot;center-block&quot;&gt;...&lt;/div&gt;</pre>
                                    <br>

                                    <p class="text-muted"><strong>Showing and hiding content</strong></p>
                                    <p>Force an element to be shown or hidden (<strong>including for screen readers</strong>) with the use of <code>.show</code> and <code>.hidden</code> classes. These classes use <code>!important</code> to avoid specificity conflicts, just like the <a href="#helper-classes-floats">quick floats</a>. They are only available for block level toggling.</p>
                                    <p><code>.hide</code> is available, but it does not always affect screen readers and is <strong>deprecated</strong> as of Bootstrap v3.0.1. Use <code>.hidden</code> or <code>.sr-only</code> instead.</p>
                                    <p>Furthermore, <code>.invisible</code> can be used to toggle only the visibility of an element, meaning its <code>display</code> is not modified and the element can still affect the flow of the document.</p>
                                    <pre class="prettyprint">&lt;div class=&quot;show&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;hidden&quot;&gt;...&lt;/div&gt;</pre>
                                    <br>

                                    <p class="text-muted"><strong>Text helper</strong></p>
                                    <p>Allows you to select the color, sizing or Font style, use with <code>!important</code>.</p>
                                    <p class="text-primary">Consequat condimentum, fusce tincidunt, faucibus ante praesent</p>
                                    <p class="text-blue">Consequat condimentum, fusce tincidunt, faucibus ante praesent</p>
                                    <p class="text-warning">Consequat condimentum, fusce tincidunt, faucibus ante praesent</p>
                                    <p class="text-red">Consequat condimentum, fusce tincidunt, faucibus ante praesent</p>
                                    <br>
                                    <p class="text-orange text-bold text-16">Consequat condimentum, fusce tincidunt, faucibus ante praesent</p>
                                    <p class="text-red text-linethrough">Consequat condimentum, fusce tincidunt, faucibus ante praesent</p>
                                    <p class="text-green text-italic text-sm">Consequat condimentum, fusce tincidunt, faucibus ante praesent</p>

                                    <pre class="prettyprint pre-scrollable">&lt;!-- Bootstrap color helper --&gt;
&lt;div class=&quot;text-primary&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;text-success&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;text-info&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;text-warning&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;text-danger&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;text-muted&quot;&gt;...&lt;/div&gt;
&lt;!-- Also avilable --&gt;
&lt;div class=&quot;text-darknight&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;text-midnight&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;text-cloud&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;text-silver&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;text-white&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;text-teal&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;text-green&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;text-orange&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;text-red&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;text-blue&quot;&gt;...&lt;/div&gt;

&lt;!-- Sizing --&gt;
&lt;div class=&quot;text-sm&quot;&gt;...&lt;/div&gt; &lt;!-- .8em of parent font-size --&gt;
&lt;div class=&quot;text-lg&quot;&gt;...&lt;/div&gt; &lt;!-- 1.2em of parent font-size --&gt;
&lt;div class=&quot;text-xg&quot;&gt;...&lt;/div&gt; &lt;!-- 1.6em of parent font-size --&gt;
&lt;div class=&quot;text-16&quot;&gt;...&lt;/div&gt; &lt;!-- 16px font-size --&gt;
&lt;div class=&quot;text-24&quot;&gt;...&lt;/div&gt; &lt;!-- 24px font-size --&gt;
&lt;div class=&quot;text-32&quot;&gt;...&lt;/div&gt; &lt;!-- 32px font-size --&gt;
&lt;div class=&quot;text-48&quot;&gt;...&lt;/div&gt; &lt;!-- 48px font-size --&gt;
&lt;div class=&quot;text-64&quot;&gt;...&lt;/div&gt; &lt;!-- 64px font-size --&gt;

&lt;!-- Styling --&gt;
&lt;div class=&quot;text-bold&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;text-italic&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;text-underline&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;text-linethrough&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;text-lead&quot;&gt;...&lt;/div&gt; &lt;!-- 300 font-weight --&gt;
&lt;div class=&quot;text-nodecor&quot;&gt;...&lt;/div&gt; &lt;!-- no decoration --&gt;</pre>
                                    <p><i class="fa fa-hand-o-up"></i> <small>use <code>.pre-scrollable</code></small></p>
                                    <br>

                                    <p class="text-muted"><strong>Shadow helper</strong></p>
                                    <p>Give a nice shadow to any element. Use with <code>.shadow</code> or disable shadow with <code>no-shadow</code>.</p>
                                    <p>
                                        <span class="demo-box shadow bg-midnight">.shadow</span>
                                        <span class="demo-box shadow bordered-flat">.shadow</span>
                                        <span class="demo-box well no-shadow" title="A .well with no shadow">.no-shadow</span>
                                    </p>
                                    <br>

                                    <p class="text-muted"><strong>Corner helper</strong></p>
                                    <p>Give <code>4px</code> border radius on any element with <code>.corner</code>. See available class below:</p>
                                    <p>
                                        <span class="demo-box shadow corner bg-midnight">.corner</span>
                                        <span class="demo-box shadow corner-top bg-primary">.corner-top</span>
                                        <span class="demo-box shadow corner-bottom bg-danger">.corner-bottom</span>
                                        <span class="demo-box shadow corner-br corner-tl bg-success">.corner-tl/br</span>
                                        <span class="demo-box well no-corner" title="A .well with no corner">.no-corner</span>
                                    </p>
                                    <pre class="prettyprint">&lt;div class=&quot;corner&quot;&gt;...&lt;/div&gt; &lt;!-- corner all --&gt;
&lt;div class=&quot;corner-top&quot;&gt;...&lt;/div&gt; &lt;!-- top corner --&gt;
&lt;div class=&quot;corner-tr&quot;&gt;...&lt;/div&gt; &lt;!-- top right corner --&gt;
&lt;div class=&quot;corner-tl&quot;&gt;...&lt;/div&gt; &lt;!-- top left corner --&gt;
&lt;div class=&quot;corner-bottom&quot;&gt;...&lt;/div&gt; &lt;!-- bottom corner --&gt;
&lt;div class=&quot;corner-br&quot;&gt;...&lt;/div&gt; &lt;!-- bottom right corner --&gt;
&lt;div class=&quot;corner-bl&quot;&gt;...&lt;/div&gt; &lt;!-- bottom left corner --&gt;

&lt;!-- Disable corner --&gt;
&lt;div class=&quot;no-corner&quot;&gt;...&lt;/div&gt;</pre>
                                </div><!--/cols -->
                            </div><!--/row -->
                        </div><!-- /panel-body -->
                    </div><!-- /panel-helpclass -->




                    <div id="panel-resutils" class="panel panel-default">
                        <div class="panel-heading">
                            <div class="panel-actions">
                                <button data-refresh="#panel-resutils" title="refresh" class="btn-panel">
                                    <i class="fa fa-refresh"></i>
                                </button>
                                <button data-expand="#panel-resutils" title="expand" class="btn-panel">
                                    <i class="fa fa-expand"></i>
                                </button>
                                <button data-collapse="#panel-resutils" title="collapse" class="btn-panel">
                                    <i class="fa fa-caret-down"></i>
                                </button>
                                <button data-close="#panel-resutils" title="close" class="btn-panel">
                                    <i class="fa fa-times"></i>
                                </button>
                            </div><!-- /panel-actions -->
                            <h3 class="panel-title">Responsive Utilities</h3>
                        </div><!-- /panel-heading -->

                        <div class="panel-body">
                            <p class="lead">For faster mobile-friendly development, use these utility classes for showing and hiding content by device via media query. Also included are utility classes for toggling content when printed.</p>
                            <p>Try to use these on a limited basis and avoid creating entirely different versions of the same site. Instead, use them to complement each device's presentation. <strong>Responsive utilities are currently only available for block and table toggling.</strong> Use with inline and table elements is currently not supported.</p>
                        </div><!-- /panel-body -->
                        <div class="table-responsive">
                            <table class="table table-bordered">
                                <thead>
                                    <tr>
                                        <th></th>
                                        <th>
                                        Extra small devices
                                        <small>Phones (&lt;768px)</small>
                                        </th>
                                        <th>
                                        Small devices
                                        <small>Tablets (&ge;768px)</small>
                                        </th>
                                        <th>
                                        Medium devices
                                        <small>Desktops (&ge;992px)</small>
                                        </th>
                                        <th>
                                        Large devices
                                        <small>Desktops (&ge;1200px)</small>
                                        </th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <th><code>.visible-xs</code></th>
                                        <td class="is-visible">Visible</td>
                                        <td class="is-hidden">Hidden</td>
                                        <td class="is-hidden">Hidden</td>
                                        <td class="is-hidden">Hidden</td>
                                    </tr>
                                    <tr>
                                        <th><code>.visible-sm</code></th>
                                        <td class="is-hidden">Hidden</td>
                                        <td class="is-visible">Visible</td>
                                        <td class="is-hidden">Hidden</td>
                                        <td class="is-hidden">Hidden</td>
                                    </tr>
                                    <tr>
                                        <th><code>.visible-md</code></th>
                                        <td class="is-hidden">Hidden</td>
                                        <td class="is-hidden">Hidden</td>
                                        <td class="is-visible">Visible</td>
                                        <td class="is-hidden">Hidden</td>
                                    </tr>
                                    <tr>
                                        <th><code>.visible-lg</code></th>
                                        <td class="is-hidden">Hidden</td>
                                        <td class="is-hidden">Hidden</td>
                                        <td class="is-hidden">Hidden</td>
                                        <td class="is-visible">Visible</td>
                                        </tr>
                                    </tbody>
                                    <tbody>
                                    <tr>
                                        <th><code>.hidden-xs</code></th>
                                        <td class="is-hidden">Hidden</td>
                                        <td class="is-visible">Visible</td>
                                        <td class="is-visible">Visible</td>
                                        <td class="is-visible">Visible</td>
                                    </tr>
                                    <tr>
                                        <th><code>.hidden-sm</code></th>
                                        <td class="is-visible">Visible</td>
                                        <td class="is-hidden">Hidden</td>
                                        <td class="is-visible">Visible</td>
                                        <td class="is-visible">Visible</td>
                                    </tr>
                                    <tr>
                                        <th><code>.hidden-md</code></th>
                                        <td class="is-visible">Visible</td>
                                        <td class="is-visible">Visible</td>
                                        <td class="is-hidden">Hidden</td>
                                        <td class="is-visible">Visible</td>
                                    </tr>
                                    <tr>
                                        <th><code>.hidden-lg</code></th>
                                        <td class="is-visible">Visible</td>
                                        <td class="is-visible">Visible</td>
                                        <td class="is-visible">Visible</td>
                                        <td class="is-hidden">Hidden</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                        <div class="panel-body">
                            <h4>Print classes</h4>
                            <p>Similar to the regular responsive classes, use these for toggling content for print.</p>
                        </div><!-- /panel-body -->
                        <div class="table-responsive">
                            <table class="table table-bordered">
                                <thead>
                                    <tr>
                                        <th>Class</th>
                                        <th>Browser</th>
                                        <th>Print</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <th><code>.visible-print</code></th>
                                        <td class="is-hidden">Hidden</td>
                                        <td class="is-visible">Visible</td>
                                    </tr>
                                    <tr>
                                        <th><code>.hidden-print</code></th>
                                        <td class="is-visible">Visible</td>
                                        <td class="is-hidden">Hidden</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div><!-- /panel-resutils -->