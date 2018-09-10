<?php

if(!isset($_SERVER['HTTP_X_PJAX'])){

    $content = basename($_SERVER['SCRIPT_NAME']);

    $_SERVER['HTTP_X_PJAX'] = true;
    include 'stilearn.base.template.php';
    die();
}

?>
                    <!-- Grid system
                    ================================================== -->
                    <p>Grid systems are used for creating page layouts through a series of rows and columns that house your content. Here's how the Bootstrap grid system works:</p>
                    <ul class="fa-ul">
                        <li><i class="fa-li fa fa-check-square"></i>Rows must be placed within a <code>.container</code> for proper alignment and padding.</li>
                        <li><i class="fa-li fa fa-check-square"></i>Use rows to create horizontal groups of columns.</li>
                        <li><i class="fa-li fa fa-check-square"></i>Content should be placed within columns, and only columns may be immediate children of rows.</li>
                        <li><i class="fa-li fa fa-check-square"></i>Predefined grid classes like <code>.row</code> and <code>.col-xs-4</code> are available for quickly making grid layouts. LESS mixins can also be used for more semantic layouts.</li>
                        <li><i class="fa-li fa fa-check-square"></i>Columns create gutters (gaps between column content) via <code>padding</code>. That padding is offset in rows for the first and last column via negative margin on <code>.row</code>s.</li>
                        <li><i class="fa-li fa fa-check-square"></i>Grid columns are created by specifying the number of twelve available columns you wish to span. For example, three equal columns would use three <code>.col-xs-4</code>.</li>
                    </ul>
                    <p>Look to the examples for applying these principles to your code.</p>

                    <div class="callout callout-info">
                        <h4>Grids and full-width layouts</h4>
                        <p>Folks looking to create fully fluid layouts (meaning your site stretches the entire width of the viewport) must wrap their grid content in a containing element with <code>padding: 0 15px;</code> to offset the <code>margin: 0 -15px;</code> used on <code>.row</code>s.</p>
                    </div>

                    <h3 id="grid-media-queries">Media queries</h3>
                    <p>Bootstrap use the following media queries in LESS files to create the key breakpoints in grid system.</p>
                    <pre class="no-padding prettyprint lang-css">/* Extra small devices (phones, less than 768px) */
/* No media query since this is the default in Bootstrap */

/* Small devices (tablets, 768px and up) */
@media (min-width: @screen-sm-min) { ... }

/* Medium devices (desktops, 992px and up) */
@media (min-width: @screen-md-min) { ... }

/* Large devices (large desktops, 1200px and up) */
@media (min-width: @screen-lg-min) { ... }</pre>
                    <p>Bootstrap occasionally expand on these media queries to include a <code>max-width</code> to limit CSS to a narrower set of devices.</p>
                    <pre class="no-padding prettyprint lang-css">@media (max-width: @screen-xs-max) { ... }
@media (min-width: @screen-sm-min) and (max-width: @screen-sm-max) { ... }
@media (min-width: @screen-md-min) and (max-width: @screen-md-max) { ... }
@media (min-width: @screen-lg-min) { ... }</pre>
                    
                    <h3 id="grid-options">Grid options</h3>
                    <p>See how aspects of the Bootstrap grid system work across multiple devices with a handy table.</p>
                    <div class="table-responsive">
                        <table class="table table-bordered table-striped">
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
                                    <th>Grid behavior</th>
                                    <td>Horizontal at all times</td>
                                    <td colspan="3">Collapsed to start, horizontal above breakpoints</td>
                                </tr>
                                <tr>
                                    <th>Max container width</th>
                                    <td>None (auto)</td>
                                    <td>750px</td>
                                    <td>970px</td>
                                    <td>1170px</td>
                                </tr>
                                <tr>
                                    <th>Class prefix</th>
                                    <td><code>.col-xs-</code></td>
                                    <td><code>.col-sm-</code></td>
                                    <td><code>.col-md-</code></td>
                                    <td><code>.col-lg-</code></td>
                                </tr>
                                <tr>
                                    <th># of columns</th>
                                    <td colspan="4">12</td>
                                </tr>
                                <tr>
                                <th>Max column width</th>
                                    <td class="text-muted">Auto</td>
                                    <td>60px</td>
                                    <td>78px</td>
                                    <td>95px</td>
                                </tr>
                                <tr>
                                    <th>Gutter width</th>
                                    <td colspan="4">30px (15px on each side of a column)</td>
                                </tr>
                                <tr>
                                    <th>Nestable</th>
                                    <td colspan="4">Yes</td>
                                </tr>
                                <tr>
                                    <th>Offsets</th>
                                    <td colspan="4">Yes</td>
                                </tr>
                                <tr>
                                    <th>Column ordering</th>
                                    <td colspan="4">Yes</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                    <p>Grid classes apply to devices with screen widths greater than or equal to the breakpoint sizes, and override grid classes targeted at smaller devices. Therefore, applying any <code>.col-md-</code> class to an element will not only affect its styling on medium devices but also on large devices if a <code>.col-lg-</code> class is not present.</p>

                    <h3>Example: Stacked-to-horizontal</h3>
                    <p>Using a single set of <code>.col-md-*</code> grid classes, you can create a basic grid system that starts out stacked on mobile devices and tablet devices (the extra small to small range) before becoming horizontal on desktop (medium) devices. Place grid columns in any <code>.row</code>.</p>
                    <div class="row show-grid">
                        <div class="col-md-1">.col-md-1</div>
                        <div class="col-md-1">.col-md-1</div>
                        <div class="col-md-1">.col-md-1</div>
                        <div class="col-md-1">.col-md-1</div>
                        <div class="col-md-1">.col-md-1</div>
                        <div class="col-md-1">.col-md-1</div>
                        <div class="col-md-1">.col-md-1</div>
                        <div class="col-md-1">.col-md-1</div>
                        <div class="col-md-1">.col-md-1</div>
                        <div class="col-md-1">.col-md-1</div>
                        <div class="col-md-1">.col-md-1</div>
                        <div class="col-md-1">.col-md-1</div>
                    </div>
                    <div class="row show-grid">
                        <div class="col-md-8">.col-md-8</div>
                        <div class="col-md-4">.col-md-4</div>
                    </div>
                    <div class="row show-grid">
                        <div class="col-md-4">.col-md-4</div>
                        <div class="col-md-4">.col-md-4</div>
                        <div class="col-md-4">.col-md-4</div>
                    </div>
                    <div class="row show-grid">
                        <div class="col-md-6">.col-md-6</div>
                        <div class="col-md-6">.col-md-6</div>
                    </div>
                    <pre class="no-padding prettyprint lang-css">&lt;div class=&quot;row&quot;&gt;
    &lt;div class=&quot;col-md-1&quot;&gt;.col-md-1&lt;/div&gt;
    &lt;div class=&quot;col-md-1&quot;&gt;.col-md-1&lt;/div&gt;
    &lt;div class=&quot;col-md-1&quot;&gt;.col-md-1&lt;/div&gt;
    &lt;div class=&quot;col-md-1&quot;&gt;.col-md-1&lt;/div&gt;
    &lt;div class=&quot;col-md-1&quot;&gt;.col-md-1&lt;/div&gt;
    &lt;div class=&quot;col-md-1&quot;&gt;.col-md-1&lt;/div&gt;
    &lt;div class=&quot;col-md-1&quot;&gt;.col-md-1&lt;/div&gt;
    &lt;div class=&quot;col-md-1&quot;&gt;.col-md-1&lt;/div&gt;
    &lt;div class=&quot;col-md-1&quot;&gt;.col-md-1&lt;/div&gt;
    &lt;div class=&quot;col-md-1&quot;&gt;.col-md-1&lt;/div&gt;
    &lt;div class=&quot;col-md-1&quot;&gt;.col-md-1&lt;/div&gt;
    &lt;div class=&quot;col-md-1&quot;&gt;.col-md-1&lt;/div&gt;
&lt;/div&gt;
&lt;div class=&quot;row&quot;&gt;
    &lt;div class=&quot;col-md-8&quot;&gt;.col-md-8&lt;/div&gt;
    &lt;div class=&quot;col-md-4&quot;&gt;.col-md-4&lt;/div&gt;
&lt;/div&gt;
&lt;div class=&quot;row&quot;&gt;
    &lt;div class=&quot;col-md-4&quot;&gt;.col-md-4&lt;/div&gt;
    &lt;div class=&quot;col-md-4&quot;&gt;.col-md-4&lt;/div&gt;
    &lt;div class=&quot;col-md-4&quot;&gt;.col-md-4&lt;/div&gt;
&lt;/div&gt;
&lt;div class=&quot;row&quot;&gt;
    &lt;div class=&quot;col-md-6&quot;&gt;.col-md-6&lt;/div&gt;
    &lt;div class=&quot;col-md-6&quot;&gt;.col-md-6&lt;/div&gt;
&lt;/div&gt;</pre>

                    <h3>Example: Mobile and desktop</h3>
                    <p>Don't want your columns to simply stack in smaller devices? Use the extra small and medium device grid classes by adding <code>.col-xs-*</code> <code>.col-md-*</code> to your columns. See the example below for a better idea of how it all works.</p>
                    <div class="row show-grid">
                        <div class="col-xs-12 col-md-8">.col-xs-12 .col-md-8</div>
                        <div class="col-xs-6 col-md-4">.col-xs-6 .col-md-4</div>
                    </div>
                    <div class="row show-grid">
                        <div class="col-xs-6 col-md-4">.col-xs-6 .col-md-4</div>
                        <div class="col-xs-6 col-md-4">.col-xs-6 .col-md-4</div>
                        <div class="col-xs-6 col-md-4">.col-xs-6 .col-md-4</div>
                    </div>
                    <div class="row show-grid">
                        <div class="col-xs-6">.col-xs-6</div>
                        <div class="col-xs-6">.col-xs-6</div>
                    </div>
                    <pre class="no-padding prettyprint lang-css">&lt;!-- Stack the columns on mobile by making one full-width and the other half-width --&gt;
&lt;div class=&quot;row&quot;&gt;
    &lt;div class=&quot;col-xs-12 col-md-8&quot;&gt;.col-xs-12 .col-md-8&lt;/div&gt;
    &lt;div class=&quot;col-xs-6 col-md-4&quot;&gt;.col-xs-6 .col-md-4&lt;/div&gt;
&lt;/div&gt;

&lt;!-- Columns start at 50% wide on mobile and bump up to 33.3% wide on desktop --&gt;
&lt;div class=&quot;row&quot;&gt;
    &lt;div class=&quot;col-xs-6 col-md-4&quot;&gt;.col-xs-6 .col-md-4&lt;/div&gt;
    &lt;div class=&quot;col-xs-6 col-md-4&quot;&gt;.col-xs-6 .col-md-4&lt;/div&gt;
    &lt;div class=&quot;col-xs-6 col-md-4&quot;&gt;.col-xs-6 .col-md-4&lt;/div&gt;
&lt;/div&gt;

&lt;!-- Columns are always 50% wide, on mobile and desktop --&gt;
&lt;div class=&quot;row&quot;&gt;
    &lt;div class=&quot;col-xs-6&quot;&gt;.col-xs-6&lt;/div&gt;
    &lt;div class=&quot;col-xs-6&quot;&gt;.col-xs-6&lt;/div&gt;
&lt;/div&gt;</pre>
                    
                    <h3>Example: Mobile, tablet, desktops</h3>
                    <p>Build on the previous example by creating even more dynamic and powerful layouts with tablet <code>.col-sm-*</code> classes.</p>
                    <div class="row show-grid">
                        <div class="col-xs-12 col-sm-6 col-md-8">.col-xs-12 .col-sm-6 .col-md-8</div>
                        <div class="col-xs-6 col-md-4">.col-xs-6 .col-md-4</div>
                    </div>
                    <div class="row show-grid">
                        <div class="col-xs-6 col-sm-4">.col-xs-6 .col-sm-4</div>
                        <div class="col-xs-6 col-sm-4">.col-xs-6 .col-sm-4</div>
                    <!-- Optional: clear the XS cols if their content doesn't match in height -->
                    <div class="clearfix visible-xs"></div>
                        <div class="col-xs-6 col-sm-4">.col-xs-6 .col-sm-4</div>
                    </div>
                    <pre class="no-padding prettyprint lang-css">&lt;div class=&quot;row&quot;&gt;
    &lt;div class=&quot;col-xs-12 col-sm-6 col-md-8&quot;&gt;.col-xs-12 .col-sm-6 .col-md-8&lt;/div&gt;
    &lt;div class=&quot;col-xs-6 col-md-4&quot;&gt;.col-xs-6 .col-md-4&lt;/div&gt;
&lt;/div&gt;
&lt;div class=&quot;row&quot;&gt;
    &lt;div class=&quot;col-xs-6 col-sm-4&quot;&gt;.col-xs-6 .col-sm-4&lt;/div&gt;
    &lt;div class=&quot;col-xs-6 col-sm-4&quot;&gt;.col-xs-6 .col-sm-4&lt;/div&gt;
    &lt;!-- Optional: clear the XS cols if their content doesn&#39;t match in height --&gt;
    &lt;div class=&quot;clearfix visible-xs&quot;&gt;&lt;/div&gt;
    &lt;div class=&quot;col-xs-6 col-sm-4&quot;&gt;.col-xs-6 .col-sm-4&lt;/div&gt;
&lt;/div&gt;</pre>
                    
                    <h3>Responsive column resets</h3>
                    <p>With the four tiers of grids available you're bound to run into issues where, at certain breakpoints, your columns don't clear quite right as one is taller than the other. To fix that, use a combination of a <code>.clearfix</code> and responsive utility classes.</p>
                    <div class="row show-grid">
                        <div class="col-xs-6 col-sm-3">
                        .col-xs-6 .col-sm-3
                        <br>
                        Resize your viewport or check it out on your phone for an example.
                    </div>
                    <div class="col-xs-6 col-sm-3">.col-xs-6 .col-sm-3</div>

                    <!-- Add the extra clearfix for only the required viewport -->
                    <div class="clearfix visible-xs"></div>

                    <div class="col-xs-6 col-sm-3">.col-xs-6 .col-sm-3</div>
                        <div class="col-xs-6 col-sm-3">.col-xs-6 .col-sm-3</div>
                    </div>
                    <pre class="no-padding prettyprint lang-css">&lt;div class=&quot;row&quot;&gt;
    &lt;div class=&quot;col-xs-6 col-sm-3&quot;&gt;.col-xs-6 .col-sm-3&lt;/div&gt;
    &lt;div class=&quot;col-xs-6 col-sm-3&quot;&gt;.col-xs-6 .col-sm-3&lt;/div&gt;

    &lt;!-- Add the extra clearfix for only the required viewport --&gt;
    &lt;div class=&quot;clearfix visible-xs&quot;&gt;&lt;/div&gt;

    &lt;div class=&quot;col-xs-6 col-sm-3&quot;&gt;.col-xs-6 .col-sm-3&lt;/div&gt;
    &lt;div class=&quot;col-xs-6 col-sm-3&quot;&gt;.col-xs-6 .col-sm-3&lt;/div&gt;
&lt;/div&gt;</pre>
                    
                    <p>In addition to column clearing at responsive breakpoints, you may need to <strong>reset offsets, pushes, or pulls</strong>. Those resets are available for medium and large grid tiers only, since they start only at the (second) small grid tier. See this in action in <a target="_blank" href="http://getbootstrap.com/examples/grid/">the grid example</a>.</p>
                    <pre class="no-padding prettyprint lang-css">&lt;div class=&quot;row&quot;&gt;
    &lt;div class=&quot;col-sm-5 col-md-6&quot;&gt;.col-sm-5 .col-md-6&lt;/div&gt;
    &lt;div class=&quot;col-sm-5 col-sm-offset-2 col-md-6 col-md-offset-0&quot;&gt;.col-sm-5 .col-sm-offset-2 .col-md-6 .col-md-offset-0&lt;/div&gt;
&lt;/div&gt;

&lt;div class=&quot;row&quot;&gt;
    &lt;div class=&quot;col-sm-6 col-md-5 col-lg-6&quot;&gt;.col-sm-6 .col-md-5 .col-lg-6&lt;/div&gt;
    &lt;div class=&quot;col-sm-6 col-md-5 col-md-offset-2 col-lg-6 col-lg-offset-0&quot;&gt;.col-sm-6 .col-md-5 .col-md-offset-2 .col-lg-6 .col-lg-offset-0&lt;/div&gt;
&lt;/div&gt;</pre>

                    <h3 id="grid-offsetting">Offsetting columns</h3>
                    <p>Move columns to the right using <code>.col-md-offset-*</code> classes. These classes increase the left margin of a column by <code>*</code> columns. For example, <code>.col-md-offset-4</code> moves <code>.col-md-4</code> over four columns.</p>
                    <div class="row show-grid">
                        <div class="col-md-4">.col-md-4</div>
                        <div class="col-md-4 col-md-offset-4">.col-md-4 .col-md-offset-4</div>
                    </div>
                    <div class="row show-grid">
                        <div class="col-md-3 col-md-offset-3">.col-md-3 .col-md-offset-3</div>
                        <div class="col-md-3 col-md-offset-3">.col-md-3 .col-md-offset-3</div>
                    </div>
                    <div class="row show-grid">
                        <div class="col-md-6 col-md-offset-3">.col-md-6 .col-md-offset-3</div>
                    </div>
                    <pre class="no-padding prettyprint lang-css">&lt;div class=&quot;row&quot;&gt;
    &lt;div class=&quot;col-md-4&quot;&gt;.col-md-4&lt;/div&gt;
    &lt;div class=&quot;col-md-4 col-md-offset-4&quot;&gt;.col-md-4 .col-md-offset-4&lt;/div&gt;
&lt;/div&gt;
&lt;div class=&quot;row&quot;&gt;
    &lt;div class=&quot;col-md-3 col-md-offset-3&quot;&gt;.col-md-3 .col-md-offset-3&lt;/div&gt;
    &lt;div class=&quot;col-md-3 col-md-offset-3&quot;&gt;.col-md-3 .col-md-offset-3&lt;/div&gt;
&lt;/div&gt;
&lt;div class=&quot;row&quot;&gt;
    &lt;div class=&quot;col-md-6 col-md-offset-3&quot;&gt;.col-md-6 .col-md-offset-3&lt;/div&gt;
&lt;/div&gt;</pre>

                    <h3 id="grid-nesting">Nesting columns</h3>
                    <p>To nest your content with the default grid, add a new <code>.row</code> and set of <code>.col-md-*</code> columns within an existing <code>.col-md-*</code> column. Nested rows should include a set of columns that add up to 12.</p>
                    <div class="row show-grid">
                        <div class="col-md-9">
                            Level 1: .col-md-9
                            <div class="row show-grid">
                                <div class="col-md-6">Level 2: .col-md-6</div>
                                <div class="col-md-6">Level 2: .col-md-6</div>
                            </div>
                        </div>
                    </div>
                    <pre class="no-padding prettyprint lang-css">&lt;div class=&quot;row&quot;&gt;
    &lt;div class=&quot;col-md-9&quot;&gt;
        Level 1: .col-md-9
        &lt;div class=&quot;row&quot;&gt;
            &lt;div class=&quot;col-md-6&quot;&gt;Level 2: .col-md-6&lt;/div&gt;
            &lt;div class=&quot;col-md-6&quot;&gt;Level 2: .col-md-6&lt;/div&gt;
        &lt;/div&gt;
    &lt;/div&gt;
&lt;/div&gt;</pre>

                    <h3 id="grid-column-ordering">Column ordering</h3>
                    <p>Easily change the order of built-in grid columns with <code>.col-md-push-*</code> and <code>.col-md-pull-*</code> modifier classes.</p>
                    <div class="row show-grid">
                        <div class="col-md-9 col-md-push-3">.col-md-9 .col-md-push-3</div>
                        <div class="col-md-3 col-md-pull-9">.col-md-3 .col-md-pull-9</div>
                    </div>
                    <pre class="no-padding prettyprint lang-css">&lt;div class=&quot;row&quot;&gt;
    &lt;div class=&quot;col-md-9 col-md-push-3&quot;&gt;.col-md-9 .col-md-push-3&lt;/div&gt;
    &lt;div class=&quot;col-md-3 col-md-pull-9&quot;&gt;.col-md-3 .col-md-pull-9&lt;/div&gt;
&lt;/div&gt;</pre>