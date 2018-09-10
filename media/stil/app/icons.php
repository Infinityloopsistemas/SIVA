<?php

if(!isset($_SERVER['HTTP_X_PJAX'])){

    $content = basename($_SERVER['SCRIPT_NAME']);

    $_SERVER['HTTP_X_PJAX'] = true;
    include 'stilearn.base.template.php';
    die();
}

?>
                    <!-- Glyphicons & Font Awesome Icons
                    ================================================== -->
                    <div class="page-header">
                        <h1 id="glyphicons">Glyphicons & Font Awesome</h1>
                    </div>
                    <div class="row">
                        <div class="col-md-12" data-toggle="sortable-widget">
                            <div id="panel-glyphs" class="panel panel-default sortable-widget-item">
                                <div class="panel-heading">
                                    <div class="panel-actions">
                                        <button data-refresh="#panel-glyphs" title="refresh" class="btn-panel">
                                            <i class="fa fa-refresh"></i>
                                        </button>
                                        <button data-expand="#panel-glyphs" title="expand" class="btn-panel">
                                            <i class="fa fa-expand"></i>
                                        </button>
                                        <button data-collapse="#panel-glyphs" title="collapse" class="btn-panel">
                                            <i class="fa fa-caret-down"></i>
                                        </button>
                                        <button data-close="#panel-glyphs" title="close" class="btn-panel">
                                            <i class="fa fa-times"></i>
                                        </button>
                                    </div><!-- /panel-actions -->
                                    <h3 class="panel-title sortable-widget-handle">Glyphicons</h3>
                                </div><!-- /panel-heading -->

                                <div class="panel-body">
                                    <p>Includes 200 glyphs in font format from the <a target="_blank" href="http://glyphicons.com/">Glyphicon</a> Halflings set. Please check <a rel="tooltip" title="Bootstrap glyphicons" target="_blank" href="http://getbootstrap.com/components/#glyphicons">Bootstrap glyphicons</a> for available glyphs.</p>
                                    <p>For performance reasons, all icons require a base class and individual icon class. To use, place the following code just about anywhere. Be sure to leave a space between the icon and text for proper padding.</p>
                                    <div class="callout callout-danger">
                                        <h4>Don't mix with other components</h4>
                                        <p>Icon classes cannot be combined with other elements. They are designed to be standalone elements.</p>
                                    </div>
                                    <pre class="no-padding prettyprint">&lt;span class=&quot;glyphicon glyphicon-search&quot;&gt;&lt;/span&gt;</pre>
                                    
                                    <p class="text-muted"><strong>Sample Usage</strong></p>
                                    <div class="btn-group">
                                        <button type="button" class="btn btn-default"><span class="glyphicon glyphicon-align-left"></span></button>
                                        <button type="button" class="btn btn-default"><span class="glyphicon glyphicon-align-center"></span></button>
                                        <button type="button" class="btn btn-default"><span class="glyphicon glyphicon-align-right"></span></button>
                                        <button type="button" class="btn btn-default"><span class="glyphicon glyphicon-align-justify"></span></button>
                                    </div>
                                    <br>
                                    <br>
                                    <div class="btn-toolbar" role="toolbar">
                                        <button type="button" class="btn btn-default btn-lg"><span class="glyphicon glyphicon-star"></span> Star</button>
                                        <button type="button" class="btn btn-default"><span class="glyphicon glyphicon-star"></span> Star</button>
                                        <button type="button" class="btn btn-default btn-sm"><span class="glyphicon glyphicon-star"></span> Star</button>
                                        <button type="button" class="btn btn-default btn-xs"><span class="glyphicon glyphicon-star"></span> Star</button>
                                    </div>
                                    <br>
                                    <pre class="no-padding prettyprint">&lt;button type=&quot;button&quot; class=&quot;btn btn-default btn-lg&quot;&gt;
    &lt;span class=&quot;glyphicon glyphicon-star&quot;&gt;&lt;/span&gt; Star
&lt;/button&gt;</pre>
                                </div><!-- /panel-body -->
                            </div><!-- /panel-glyphs -->


                            <div id="panel-faicons" class="panel panel-default sortable-widget-item">
                                <div class="panel-heading">
                                    <div class="panel-actions">
                                        <button data-refresh="#panel-faicons" title="refresh" class="btn-panel">
                                            <i class="fa fa-refresh"></i>
                                        </button>
                                        <button data-expand="#panel-faicons" title="expand" class="btn-panel">
                                            <i class="fa fa-expand"></i>
                                        </button>
                                        <button data-collapse="#panel-faicons" title="collapse" class="btn-panel">
                                            <i class="fa fa-caret-down"></i>
                                        </button>
                                        <button data-close="#panel-faicons" title="close" class="btn-panel">
                                            <i class="fa fa-times"></i>
                                        </button>
                                    </div><!-- /panel-actions -->
                                    <h3 class="panel-title sortable-widget-handle">Font Awesome Icons</h3>
                                </div><!-- /panel-heading -->

                                <div class="panel-body">
                                    <p>The complete set of 369 icons in Font Awesome 4.0.3. Please check <a rel="tooltip" title="Font Awesome Icons" target="_blank" href="http://fortawesome.github.io/Font-Awesome/icons/">Font Awesome</a> for available Icons. You can place Font Awesome icons just about anywhere with the <code>&lt;i&gt;</code> or <code>&lt;span&gt;</code> tag.</p>
                                    <p class="text-muted"><strong>Usage Icons</strong></p>
                                    <p>To increase icon sizes relative to their container, use the <code>.fa-lg</code> (33% increase), <code>.fa-2x</code>, <code>.fa-3x</code>, <code>.fa-4x</code>, or <code>.fa-5x</code> classes.</p>
                                    <p><i class="fa fa-camera-retro fa-lg"></i> fa-camera-retro</p>
                                    <p><i class="fa fa-camera-retro fa-2x"></i> fa-camera-retro</p>
                                    <p><i class="fa fa-camera-retro fa-3x"></i> fa-camera-retro</p>
                                    <p><i class="fa fa-camera-retro fa-4x"></i> fa-camera-retro</p>
                                    <p><i class="fa fa-camera-retro fa-5x"></i> fa-camera-retro</p>
                                    <div class="callout callout-info">
                                        <p><i class="fa fa-info-circle"></i> If your icons are getting chopped off on top and bottom, make sure you have sufficient line-height.</p>
                                    </div>
                                    <pre class="no-padding prettyprint">&lt;p&gt;&lt;i class=&quot;fa fa-camera-retro fa-lg&quot;&gt;&lt;/i&gt; fa-camera-retro&lt;/p&gt;
&lt;p&gt;&lt;i class=&quot;fa fa-camera-retro fa-2x&quot;&gt;&lt;/i&gt; fa-camera-retro&lt;/p&gt;
&lt;p&gt;&lt;i class=&quot;fa fa-camera-retro fa-3x&quot;&gt;&lt;/i&gt; fa-camera-retro&lt;/p&gt;
&lt;p&gt;&lt;i class=&quot;fa fa-camera-retro fa-4x&quot;&gt;&lt;/i&gt; fa-camera-retro&lt;/p&gt;
&lt;p&gt;&lt;i class=&quot;fa fa-camera-retro fa-5x&quot;&gt;&lt;/i&gt; fa-camera-retro&lt;/p&gt;</pre>

                                    <p class="text-muted"><strong>Fixed Width Icons</strong></p>
                                    <p>Use <code>.fa-fw</code> to set icons at a fixed width. Great to use when variable icon widths throw off alignment. Especially useful in things like nav lists.</p>
                                    <ul class="nav nav-pills nav-stacked" style="width:200px">
                                        <li class="active"><a href="#"><i class="fa fa-home fa-fw"></i> Home</a></li>
                                        <li><a href="#"><i class="fa fa-book fa-fw"></i> Library</a></li>
                                        <li><a href="#"><i class="fa fa-pencil fa-fw"></i> Applications</a></li>
                                        <li><a href="#"><i class="fa fa-cogs fa-fw"></i> Settings</a></li>
                                    </ul>
                                    <br>
                                    <pre class="no-padding prettyprint">&lt;ul class=&quot;nav nav-pills nav-stacked&quot;&gt;
    &lt;li class=&quot;active&quot;&gt;&lt;a href=&quot;#&quot;&gt;&lt;i class=&quot;fa fa-home fa-fw&quot;&gt;&lt;/i&gt; Home&lt;/a&gt;&lt;/li&gt;
    &lt;li&gt;&lt;a href=&quot;#&quot;&gt;&lt;i class=&quot;fa fa-book fa-fw&quot;&gt;&lt;/i&gt; Library&lt;/a&gt;&lt;/li&gt;
    &lt;li&gt;&lt;a href=&quot;#&quot;&gt;&lt;i class=&quot;fa fa-pencil fa-fw&quot;&gt;&lt;/i&gt; Applications&lt;/a&gt;&lt;/li&gt;
    &lt;li&gt;&lt;a href=&quot;#&quot;&gt;&lt;i class=&quot;fa fa-cogs fa-fw&quot;&gt;&lt;/i&gt; Settings&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;</pre>

                                    <p class="text-muted"><strong>Bordered & Pulled Icons</strong></p>
                                    <p>Use <code>.fa-border</code> and <code>pull-right</code> or <code>pull-left</code> for easy pull quotes or article graphics.</p>
                                    <p class="clearfix"><i class="fa fa-quote-left fa-2x pull-left fa-border"></i> Use a few styles together and you'll have easy pull quotes or a great introductory article icon. Lorem ipsum dolor sit amet, consectetur adipisicing elit. Explicabo, praesentium, recusandae eligendi rem sit id voluptates suscipit quae nemo inventore ut totam minima eaque tempore doloremque incidunt officiis quidem expedita.</p>
                                    <br>
                                    <pre class="no-padding prettyprint">&lt;i class=&quot;fa fa-quote-left fa-2x pull-left fa-border&quot;&gt;&lt;/i&gt;
Use a few styles together and you&#39;ll have easy pull quotes or a great introductory article icon.</pre>

                                    <p class="text-muted"><strong>Spinning Icons</strong></p>
                                    <p>Use the <code>fa-spin</code> class to get any icon to rotate. Works well with <code>fa-spinner</code>, <code>fa-refresh</code>, and <code>fa-cog</code>.</p>
                                    <p>
                                        <button class="btn btn-default btn-lg"><i class="fa fa-spinner fa-spin"></i></button>
                                        <button class="btn btn-default btn-lg"><i class="fa fa-refresh fa-spin"></i></button>
                                        <button class="btn btn-default btn-lg"><i class="fa fa-cog fa-spin"></i></button>
                                    </p>
                                    <pre class="no-padding prettyprint">&lt;iclass=&quot;fa fa-spinner fa-spin&quot;&gt;&lt;/i&gt;
&lt;iclass=&quot;fa fa-refresh fa-spin&quot;&gt;&lt;/i&gt;
&lt;iclass=&quot;fa fa-cog fa-spin&quot;&gt;&lt;/i&gt;</pre>

                                    <p class="text-muted"><strong>Rotated &amp; Flipped</strong></p>
                                    <p>To arbitrarily rotate and flip icons, use the <code>fa-rotate-*</code> and <code>fa-flip-*</code> classes.</p>
                                    <p class="text-xg">
                                        <i class="fa fa-shield"></i>&nbsp; normal<br>
                                        <i class="fa fa-shield fa-rotate-90"></i>&nbsp; fa-rotate-90<br>
                                        <i class="fa fa-shield fa-rotate-180"></i>&nbsp; fa-rotate-180<br>
                                        <i class="fa fa-shield fa-rotate-270"></i>&nbsp; fa-rotate-270<br>
                                        <i class="fa fa-shield fa-flip-horizontal"></i>&nbsp; fa-flip-horizontal<br>
                                        <i class="fa fa-shield fa-flip-vertical"></i>&nbsp; fa-flip-vertical
                                    </p>
                                    <pre class="no-padding prettyprint">&lt;i class=&quot;fa fa-shield&quot;&gt;&lt;/i&gt;&amp;nbsp; normal&lt;br&gt;
&lt;i class=&quot;fa fa-shield fa-rotate-90&quot;&gt;&lt;/i&gt;&amp;nbsp; fa-rotate-90&lt;br&gt;
&lt;i class=&quot;fa fa-shield fa-rotate-180&quot;&gt;&lt;/i&gt;&amp;nbsp; fa-rotate-180&lt;br&gt;
&lt;i class=&quot;fa fa-shield fa-rotate-270&quot;&gt;&lt;/i&gt;&amp;nbsp; fa-rotate-270&lt;br&gt;
&lt;i class=&quot;fa fa-shield fa-flip-horizontal&quot;&gt;&lt;/i&gt;&amp;nbsp; fa-flip-horizontal&lt;br&gt;
&lt;i class=&quot;fa fa-shield fa-flip-vertical&quot;&gt;&lt;/i&gt;&amp;nbsp; icon-flip-vertical</pre>

                                    <p class="text-muted"><strong>Stacked Icons</strong></p>
                                    <p>To stack multiple icons, use the <code>fa-stack</code> class on the parent, the <code>fa-stack-1x</code> for the regularly sized icon, and <code>fa-stack-2x</code> for the larger icon. <code>fa-inverse</code> can be used as an alternative icon color. You can even throw larger icon classes on the parent to get further control of sizing.</p>
                                    <p>
                                        <span class="fa-stack fa-lg">
                                            <i class="fa fa-square-o fa-stack-2x"></i>
                                            <i class="fa fa-twitter fa-stack-1x"></i>
                                        </span> fa-twitter on fa-square-o<br>
                                        <span class="fa-stack fa-lg">
                                            <i class="fa fa-circle fa-stack-2x"></i>
                                            <i class="fa fa-flag fa-stack-1x fa-inverse"></i>
                                        </span> fa-flag on fa-circle<br>
                                        <span class="fa-stack fa-lg">
                                            <i class="fa fa-square fa-stack-2x"></i>
                                            <i class="fa fa-terminal fa-stack-1x fa-inverse"></i>
                                        </span> fa-terminal on fa-square<br>
                                        <span class="fa-stack fa-lg">
                                            <i class="fa fa-camera fa-stack-1x"></i>
                                            <i class="fa fa-ban fa-stack-2x text-danger"></i>
                                        </span> fa-ban on fa-camera
                                    </p>
                                    <pre class="no-padding prettyprint">&lt;span class=&quot;fa-stack fa-lg&quot;&gt;
    &lt;i class=&quot;fa fa-square-o fa-stack-2x&quot;&gt;&lt;/i&gt;
    &lt;i class=&quot;fa fa-twitter fa-stack-1x&quot;&gt;&lt;/i&gt;
&lt;/span&gt; fa-twitter on fa-square-o&lt;br&gt;

&lt;span class=&quot;fa-stack fa-lg&quot;&gt;
    &lt;i class=&quot;fa fa-circle fa-stack-2x&quot;&gt;&lt;/i&gt;
    &lt;i class=&quot;fa fa-flag fa-stack-1x fa-inverse&quot;&gt;&lt;/i&gt;
&lt;/span&gt; fa-flag on fa-circle&lt;br&gt;

&lt;span class=&quot;fa-stack fa-lg&quot;&gt;
    &lt;i class=&quot;fa fa-square fa-stack-2x&quot;&gt;&lt;/i&gt;
    &lt;i class=&quot;fa fa-terminal fa-stack-1x fa-inverse&quot;&gt;&lt;/i&gt;
&lt;/span&gt; fa-terminal on fa-square&lt;br&gt;

&lt;span class=&quot;fa-stack fa-lg&quot;&gt;
    &lt;i class=&quot;fa fa-camera fa-stack-1x&quot;&gt;&lt;/i&gt;
    &lt;i class=&quot;fa fa-ban fa-stack-2x text-danger&quot;&gt;&lt;/i&gt;
&lt;/span&gt; fa-ban on fa-camera</pre>

                                    <p class="text-muted"><strong>Custom CSS</strong></p>
                                    <p>Anything you can do with CSS font styles, you can do with Font Awesome. Star Ratings (inspired by <a href="http://css-tricks.com/star-ratings/" target="_blank">CSS Tricks</a>)</p>
                                    <p>
                                        <span class="rating">
                                            <span class="star"></span><span class="star"></span><span class="star"></span><span class="star"></span><span class="star"></span>
                                        </span>
                                    </p>
                                    <p>
                                        <span class="rating rating-primary">
                                            <span class="star"></span><span class="star"></span><span class="star"></span><span class="star"></span><span class="star"></span>
                                        </span>
                                    </p>
                                    <p>
                                        <span class="rating rating-success">
                                            <span class="star"></span><span class="star"></span><span class="star"></span><span class="star"></span><span class="star"></span>
                                        </span>
                                    </p>
                                    <p>
                                        <span class="rating rating-info">
                                            <span class="star"></span><span class="star"></span><span class="star"></span><span class="star"></span><span class="star"></span>
                                        </span>
                                    </p>
                                    <p>
                                        <span class="rating rating-warning">
                                            <span class="star"></span><span class="star"></span><span class="star"></span><span class="star"></span><span class="star"></span>
                                        </span>
                                    </p>
                                    <p>
                                        <span class="rating rating-danger">
                                            <span class="star"></span><span class="star"></span><span class="star"></span><span class="star"></span><span class="star"></span>
                                        </span>
                                    </p>
                                </div><!-- /panel-body -->
                            </div><!-- /panel-faicons -->
                        </div><!--/cols -->
                    </div><!--/row -->