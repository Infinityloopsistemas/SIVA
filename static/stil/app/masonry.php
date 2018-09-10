<?php

if(!isset($_SERVER['HTTP_X_PJAX'])){

    $content = basename($_SERVER['SCRIPT_NAME']);

    $_SERVER['HTTP_X_PJAX'] = true;
    include 'stilearn.base.template.php';
    die();
}

?>
                    <!-- MASONRY
                    ====================== -->
                    <div class="panel panel-default">
                    	<div class="panel-body">
                    		<p>Masonry used with <code>.masonry</code> as a container and <code>.masonry-item</code> as a item(s). Fully support with bootstrap grid (recomended to use <code>.container-fluid</code> for best results). Below is Example using bootstrap grid:</p>

                    		<pre class="no-padding prettyprint">&lt;div class=&quot;container-fluid&quot;&gt;
  /* attribute id just used for targeting if you use masonry with feature(s) */
  &lt;div class=&quot;row masonry&quot; id=&quot;masonry-sample&quot;&gt; 
    &lt;div class=&quot;col-md-6 masonry-element&quot;&gt;...&lt;/div&gt;
    &lt;div class=&quot;col-md-3 masonry-element&quot;&gt;...&lt;/div&gt;
    &lt;div class=&quot;col-md-3 masonry-element&quot;&gt;...&lt;/div&gt;
    &lt;div class=&quot;col-md-3 masonry-element&quot;&gt;...&lt;/div&gt;
    &lt;div class=&quot;col-md-3 masonry-element&quot;&gt;...&lt;/div&gt;
    &lt;div class=&quot;col-md-6 masonry-element&quot;&gt;...&lt;/div&gt;
  &lt;/div&gt;
&lt;/div&gt;</pre>

						<p><strong>GOOD NEWS: </strong>We are also add some features to masonry (Sorting, Filtering and Searching) that can be used easily. See best practice using masonry features on <a data-pjax=".content-body" href="page-gallery.php">Gallery Page</a>.</p>

						<p class="text-muted"><strong>Sorting</strong></p>
						<p>Best use on input element (recomended using input radio), with required <code>name="masonry-sort"</code>, <code>data-masonry-target="#masonry-id"</code>, <code>data-sort-attr="attr-name"</code> and <code>value="optValue"</code> (optValue: false, asc, desc). Required add <code>data-sort-attr</code> value as an attribute on <code>.masonry-item</code>.</p>
						<pre class="no-padding prettyprint">&lt;div class=&quot;btn-group&quot; data-toggle=&quot;buttons&quot;&gt;
  &lt;label class=&quot;btn btn-default&quot;&gt;
    &lt;input type=&quot;radio&quot; name=&quot;masonry-filter&quot; data-masonry-target=&quot;#masonry-sample&quot; value=&quot;false&quot; checked&gt; View all
  &lt;/label&gt;
  &lt;label class=&quot;btn btn-default&quot;&gt;
    &lt;input type=&quot;radio&quot; name=&quot;masonry-filter&quot; data-masonry-target=&quot;#masonry-sample&quot; data-sort-attr=&quot;data-name&quot; value=&quot;asc&quot;&gt; Large
  &lt;/label&gt;
  &lt;label class=&quot;btn btn-default&quot;&gt;
    &lt;input type=&quot;radio&quot; name=&quot;masonry-filter&quot; data-masonry-target=&quot;#masonry-sample&quot; data-sort-attr=&quot;data-name&quot; value=&quot;desc&quot;&gt; Medium
  &lt;/label&gt;
&lt;/div&gt;&lt;!--/btn-group--&gt;

&lt;div class=&quot;container-fluid&quot;&gt;
  &lt;div class=&quot;row masonry&quot; id=&quot;masonry-sample&quot;&gt; 
    &lt;div class=&quot;col-md-6 masonry-element&quot; data-name=&quot;lorem&quot;&gt;...&lt;/div&gt;
    &lt;div class=&quot;col-md-3 masonry-element&quot; data-name=&quot;ipsum&quot;&gt;...&lt;/div&gt;
    &lt;div class=&quot;col-md-3 masonry-element&quot; data-name=&quot;dolor&quot;&gt;...&lt;/div&gt;
  &lt;/div&gt;
&lt;/div&gt;</pre>
						

						<p class="text-muted"><strong>Filtering</strong></p>
						<p>Best use on input element (recomended using input radio), with required <code>name="masonry-filter"</code>, <code>data-masonry-target="#masonry-id"</code> and <code>value="filter-value"</code>. Also required <code>data-filter="filter-value"</code> on <code>.masonry-item</code>.</p>
						<pre class="no-padding prettyprint">&lt;div class=&quot;btn-group&quot; data-toggle=&quot;buttons&quot;&gt;
  &lt;label class=&quot;btn btn-default&quot;&gt;
    &lt;input type=&quot;radio&quot; name=&quot;masonry-filter&quot; data-masonry-target=&quot;#masonry-sample&quot; value=&quot;all&quot; checked&gt; View all
  &lt;/label&gt;
  &lt;label class=&quot;btn btn-default&quot;&gt;
    &lt;input type=&quot;radio&quot; name=&quot;masonry-filter&quot; data-masonry-target=&quot;#masonry-sample&quot; value=&quot;filter1&quot;&gt; Large
  &lt;/label&gt;
  &lt;label class=&quot;btn btn-default&quot;&gt;
    &lt;input type=&quot;radio&quot; name=&quot;masonry-filter&quot; data-masonry-target=&quot;#masonry-sample&quot; value=&quot;filter2&quot;&gt; Medium
  &lt;/label&gt;
&lt;/div&gt;&lt;!--/btn-group--&gt;

&lt;div class=&quot;container-fluid&quot;&gt;
  &lt;div class=&quot;row masonry&quot; id=&quot;masonry-sample&quot;&gt; 
    &lt;div class=&quot;col-md-6 masonry-element&quot; data-filter=&quot;filter1&quot;&gt;...&lt;/div&gt;
    &lt;div class=&quot;col-md-3 masonry-element&quot; data-filter=&quot;filter2&quot;&gt;...&lt;/div&gt;
    &lt;div class=&quot;col-md-3 masonry-element&quot; data-filter=&quot;filter1&quot;&gt;...&lt;/div&gt;
  &lt;/div&gt;
&lt;/div&gt;</pre>


						<p class="text-muted"><strong>Searching</strong></p>
						<p>See example template below for used masonry with searching (the existing attributes is required).</p>
						<pre class="no-padding prettyprint">&lt;form action=&quot;#&quot; role=&quot;form&quot; name=&quot;masonry-search&quot;&gt;
  &lt;div class=&quot;input-group input-group-in&quot;&gt;
    &lt;input type=&quot;text&quot; class=&quot;form-control&quot; name=&quot;masonry-search&quot; data-search-attr=&quot;data-tags&quot; data-masonry-target=&quot;#masonry-sample&quot; placeholder=&quot;Search item...&quot; &gt;
    &lt;span class=&quot;input-group-btn&quot;&gt;
      &lt;button class=&quot;btn btn-default&quot; data-toggle=&quot;masonry-search-submit&quot;&gt;&lt;i class=&quot;fa fa-picture-o&quot;&gt;&lt;/i&gt;&lt;/button&gt;
      &lt;button class=&quot;btn btn-default hide&quot; data-toggle=&quot;masonry-search-clear&quot; data-masonry-target=&quot;#masonry-sample&quot;&gt;&lt;i class=&quot;fa fa-times&quot;&gt;&lt;/i&gt;&lt;/button&gt;
    &lt;/span&gt;
  &lt;/div&gt;
&lt;/form&gt;

&lt;div class=&quot;container-fluid&quot;&gt;
  &lt;div class=&quot;row masonry&quot; id=&quot;masonry-sample&quot;&gt; 
    &lt;div class=&quot;col-md-6 masonry-element&quot; data-tags=&quot;lorem, ipsum, dolor&quot;&gt;...&lt;/div&gt;
    &lt;div class=&quot;col-md-3 masonry-element&quot; data-tags=&quot;sit, amet&quot;&gt;...&lt;/div&gt;
    &lt;div class=&quot;col-md-3 masonry-element&quot; data-tags=&quot;dolor, amet&quot;&gt;...&lt;/div&gt;
  &lt;/div&gt;
&lt;/div&gt;</pre>
                    	</div><!--/panel-body-->
                    </div><!--/panel-->


                    <div class="page-header">
                    	<h3>Simple Masonry Exaple</h3>
                    </div>

                    <div class="btn-toolbar">
                    	<div class="btn-group btn-group-sm margin-bottom" data-toggle="buttons">
                    		<label class="btn btn-default">
                    			<input type="radio" name="masonry-filter" data-masonry-target="#masonry-sample" value="all" checked> View all
                			</label>
                    		<label class="btn btn-default">
                    			<input type="radio" name="masonry-filter" data-masonry-target="#masonry-sample" value="red"> Red
                    		</label>
                    		<label class="btn btn-default">
                    			<input type="radio" name="masonry-filter" data-masonry-target="#masonry-sample" value="blue"> Blue
                			</label>
                    	</div><!--/btn-group-->

                    	<div class="btn-group btn-group-sm pull-right margin-bottom" data-toggle="buttons">
                    		<label class="btn btn-default">
                    			<input type="radio" name="masonry-sort" data-masonry-target="#masonry-sample" value="false" checked> Default Sort
                			</label>
                			<label class="btn btn-default">
                    			<input type="radio" name="masonry-sort" data-masonry-target="#masonry-sample" data-sort-attr="data-sort" value="asc" checked> Sort <i class="fa fa-caret-up"></i>
                			</label>
                    		<label class="btn btn-default">
                    			<input type="radio" name="masonry-sort" data-masonry-target="#masonry-sample" data-sort-attr="data-sort" value="desc"> Sort <i class="fa fa-caret-down"></i>
                    		</label>
                    	</div><!--/btn-group-->
                    </div><!--/btn-toolbar-->

                    <div class="container-fluid">
                    	<div class="row masonry" id="masonry-sample">
                    		<div class="col-sm-3 col-xs-12 masonry-item helper-block-xs absolute-center bg-success" data-sort="1">
                    			<div class="absolute-center-item text-32">1</div>
                    		</div><!--/cols & .masonry-item-->

                    		<div class="col-sm-6 col-xs-12 masonry-item helper-block-md absolute-center bg-primary" data-sort="4">
                    			<div class="absolute-center-item text-32">4</div>
                    		</div><!--/cols & .masonry-item-->

                    		<div class="col-sm-3 col-xs-12 masonry-item helper-block-xs absolute-center bg-info" data-filter="blue" data-sort="6">
                    			<div class="absolute-center-item text-32">6</div>
                    		</div><!--/cols & .masonry-item-->

                    		<div class="col-sm-3 col-xs-12 masonry-item helper-block-xs absolute-center bg-warning" data-sort="3">
                    			<div class="absolute-center-item text-32">3</div>
                    		</div><!--/cols & .masonry-item-->

                    		<div class="col-sm-3 col-xs-12 masonry-item helper-block-xs absolute-center bg-danger" data-filter="red" data-sort="7">
                    			<div class="absolute-center-item text-32">7</div>
                    		</div><!--/cols & .masonry-item-->

                    		<div class="col-sm-3 col-xs-12 masonry-item helper-block-xs absolute-center bg-info" data-filter="blue" data-sort="2">
                    			<div class="absolute-center-item text-32">2</div>
                    		</div><!--/cols & .masonry-item-->

                    		<div class="col-sm-3 col-xs-12 masonry-item helper-block-xs absolute-center bg-danger" data-filter="red" data-sort="5">
                    			<div class="absolute-center-item text-32">5</div>
                    		</div><!--/cols & .masonry-item-->
                    	</div><!--/row & .masonry-->
                    </div><!--/container-fluid-->