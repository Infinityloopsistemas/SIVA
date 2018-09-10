<?php

if(!isset($_SERVER['HTTP_X_PJAX'])){

    $content = basename($_SERVER['SCRIPT_NAME']);

    $_SERVER['HTTP_X_PJAX'] = true;
    include 'stilearn.base.template.php';
    die();
}

?>
                    <!-- GALLERY
                    ================================================== -->
                    <div class="btn-toolbar">
                    	<div class="btn-group btn-group-sm margin-bottom" data-toggle="buttons">
                    		<label class="btn btn-default">
                    			<input type="radio" name="masonry-filter" data-masonry-target="#gallery" value="all" checked> View all
                			</label>
                    		<label class="btn btn-default">
                    			<input type="radio" name="masonry-filter" data-masonry-target="#gallery" value="large"> Large
                    		</label>
                    		<label class="btn btn-default">
                    			<input type="radio" name="masonry-filter" data-masonry-target="#gallery" value="medium"> Medium
                			</label>
                    		<label class="btn btn-default">
                    			<input type="radio" name="masonry-filter" data-masonry-target="#gallery" value="small"> Small
                			</label>
                    	</div><!--/btn-group-->

                    	<div class="btn-group btn-group-sm pull-right margin-bottom" data-toggle="buttons">
                    		<label class="btn btn-default">
                    			<input type="radio" name="masonry-sort" data-masonry-target="#gallery" value="false" checked> Default Sort
                			</label>
                			<label class="btn btn-default">
                    			<input type="radio" name="masonry-sort" data-masonry-target="#gallery" data-sort-attr="data-name" value="asc" checked> Sort <i class="fa fa-caret-up"></i>
                			</label>
                    		<label class="btn btn-default">
                    			<input type="radio" name="masonry-sort" data-masonry-target="#gallery" data-sort-attr="data-name" value="desc"> Sort <i class="fa fa-caret-down"></i>
                    		</label>
                    	</div><!--/btn-group-->
                    </div><!--/btn-toolbar-->


	            	<form action="#" role="form" name="masonry-search">
	            		<div class="input-group input-group-in">
	            			<input type="text" class="form-control helper-inline input-lg" name="masonry-search" data-search-attr="data-tags" data-masonry-target="#gallery" placeholder="Search image..." >
	            			<span class="input-group-btn">
	            				<button class="btn btn-primary text-muted" data-toggle="masonry-search-submit"><i class="fa fa-picture-o"></i></button>
	            				<button class="btn btn-primary text-muted hide" data-toggle="masonry-search-clear" data-masonry-target="#gallery"><i class="fa fa-times"></i></button>
	            			</span>
	            		</div>
	            	</form>

                	<div class="container-fluid">
                    	<div class="gallery-wrapper row masonry" id="gallery">
	            			<div class="gallery-item masonry-item col-lg-3 col-md-4 col-sm-6 col-xs-12 h-2x" data-filter="large" data-name="a" data-tags="Culpa, voluptatibus, nam, illo, sapiente, id molestias, large">
	            				<a class="gallery-image" href="#" data-toggle="gallery-expand">
	            					<img class="lazy" data-original="images/dummy/img1.png" alt="Gallery image" />
	            				</a><!--/gallery-image-->

	            				<div class="gallery-caption">
	            					<p>Commodi, cupiditate, obcaecati</p>
	            					<p class="pull-right">
	            						<a href="#"><i class="fa fa-heart"></i> 67</a> &nbsp;&nbsp; <a href="#"><i class="fa fa-comments"></i> 34</a>
	            					</p>
	            				</div><!--/gallery-caption-->

	            				<div class="gallery-item-expand">
	            					<div class="gi-actions btn-group">
	            						<div class="btn-group">
		            						<button href="#" class="btn btn-cloud btn-xs dropdown-toggle" data-toggle="dropdown">
		            							<i class="fa fa-ellipsis-h"></i>
	            							</button>
	            							<ul class="dropdown-menu pull-right" role="menu">
	            								<li><a href="#">Download</a></li>
	            								<li><a href="#">Share</a></li>
	            								<li><a href="#">Edit</a></li>
	            								<li class="divider"></li>
	            								<li><a href="#">Something else</a></li>
	            							</ul>
	            						</div><!--/btn-group-->
	            						<button href="#" class="btn btn-cloud btn-xs hidden-md hidden-lg" data-toggle="gallery-expand-caption"><i class="fa fa-th-large"></i></button>
	            						<button href="#" class="btn btn-cloud btn-xs" data-toggle="gallery-expand-close"><i class="fa fa-times"></i></button>
	            					</div><!--/gallery-actions-->

	            					<a href="#" class="gi-control-right">
	            						<i class="fa fa-angle-right text-64"></i>
	            					</a><!--/gallery-control-right-->

	            					<a href="#" class="gi-control-left">
	            						<i class="fa fa-angle-left text-64"></i>
	            					</a><!--/gallery-control-right-->

	            					<div class="gi-expand-img">
	            						<img class="lazy" data-original="images/dummy/img1.png" alt="Gallery image" />
	            					</div><!--/gallery-expand-image-->

	            					<div class="panel panel-default bg-inverse">
	            						<div class="panel-body">
	            							<div class="profile-line clearfix">
												<img class="img-circle pull-left" src="images/dummy/uifaces14.jpg" alt="uifaces14" width="46px"/>
												<div class="text-14"><strong>Kathy Reynolds</strong></div>
												<div class="text-muted"><small>Upload on Feb 5, 2014</small></div>
											</div><!--/profile-line-->
	            							<p>Text Caption Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sed, pariatur, iusto ex eius delectus odit dolore ducimus accusantium nostrum enim esse beatae nihil rem quam fuga tempore nisi harum cupiditate?</p>
	            						</div><!--/panel-body-->
	            						<ul class="list-group">
                                            <li class="list-group-item">
                                                <div class="pull-right">location/path</div>
                                                Folder
                                            </li>
                                            <li class="list-group-item">
                                                <div class="pull-right">640 x 480</div>
                                                Dimantions
                                            </li>
                                            <li class="list-group-item">
                                                <div class="pull-right">image-name.jpg</div>
                                                File name
                                            </li>
                                            <li class="list-group-item">
                                                <div class="pull-right">16 Kb</div>
                                                File size
                                            </li>
                                            <li class="list-group-item">
                                                <div class="pull-right">Feb 20, 2014</div>
                                                Update
                                            </li>
                                            <li class="list-group-item">
                                                <small><code>http://site.com/path/image-name.jpg</code></small>
                                            </li>
                                        </ul>
	            					</div><!--/panel as details caption-->
	            				</div><!--/gallery-item-expand-->
	            			</div><!--/gallery-item-->

	            			<div class="gallery-item masonry-item col-lg-3 col-md-4 col-sm-6 col-xs-12" data-filter="large" data-name="b" data-tags="Illo, fuga, voluptates, doloribus, voluptatum, non, numquam, large">
	            				<a class="gallery-image" href="#" data-toggle="gallery-expand">
	            					<img class="lazy" data-original="images/dummy/img2.png" alt="Gallery image" />
	            				</a><!--/gallery-image-->

	            				<div class="gallery-caption">
	            					<p>Commodi, cupiditate, obcaecati</p>
	            					<p class="pull-right">
	            						<a href="#"><i class="fa fa-heart"></i> 67</a> &nbsp;&nbsp; <a href="#"><i class="fa fa-comments"></i> 34</a>
	            					</p>
	            				</div><!--/gallery-caption-->

	            				<div class="gallery-item-expand">
	            					<div class="gi-actions btn-group">
	            						<div class="btn-group">
		            						<button href="#" class="btn btn-cloud btn-xs dropdown-toggle" data-toggle="dropdown">
		            							<i class="fa fa-ellipsis-h"></i>
	            							</button>
	            							<ul class="dropdown-menu pull-right" role="menu">
	            								<li><a href="#">Download</a></li>
	            								<li><a href="#">Share</a></li>
	            								<li><a href="#">Edit</a></li>
	            								<li class="divider"></li>
	            								<li><a href="#">Something else</a></li>
	            							</ul>
	            						</div><!--/btn-group-->
	            						<button href="#" class="btn btn-cloud btn-xs hidden-md hidden-lg" data-toggle="gallery-expand-caption"><i class="fa fa-th-large"></i></button>
	            						<button href="#" class="btn btn-cloud btn-xs" data-toggle="gallery-expand-close"><i class="fa fa-times"></i></button>
	            					</div><!--/gallery-actions-->

	            					<a href="#" class="gi-control-right">
	            						<i class="fa fa-angle-right text-64"></i>
	            					</a><!--/gallery-control-right-->

	            					<a href="#" class="gi-control-left">
	            						<i class="fa fa-angle-left text-64"></i>
	            					</a><!--/gallery-control-right-->

	            					<div class="gi-expand-img">
	            						<img class="lazy" data-original="images/dummy/img2.png" alt="Gallery image" />
	            					</div><!--/gallery-expand-image-->

	            					<div class="panel panel-default bg-inverse">
	            						<div class="panel-body">
	            							<div class="profile-line clearfix">
		                                        <img class="img-circle pull-left" src="images/dummy/uifaces11.jpg" alt="uifaces11" width="46px" width="46px" />
		                                        <div class="text-14"><strong>Samantha Jenkins</strong></div>
		                                        <div class="text-muted"><small>Upload on Feb 5, 2014</small></div>
		                                    </div><!--/profile-line-->
	            							<p>Text Caption Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sed, pariatur, iusto ex eius delectus odit dolore ducimus accusantium nostrum enim esse beatae nihil rem quam fuga tempore nisi harum cupiditate?</p>
	            						</div><!--/panel-body-->
	            						<ul class="list-group">
                                            <li class="list-group-item">
                                                <div class="pull-right">location/path</div>
                                                Folder
                                            </li>
                                            <li class="list-group-item">
                                                <div class="pull-right">640 x 480</div>
                                                Dimantions
                                            </li>
                                            <li class="list-group-item">
                                                <div class="pull-right">image-name.jpg</div>
                                                File name
                                            </li>
                                            <li class="list-group-item">
                                                <div class="pull-right">16 Kb</div>
                                                File size
                                            </li>
                                            <li class="list-group-item">
                                                <div class="pull-right">Feb 20, 2014</div>
                                                Update
                                            </li>
                                            <li class="list-group-item">
                                                <small><code>http://site.com/path/image-name.jpg</code></small>
                                            </li>
                                        </ul>
	            					</div><!--/panel as details caption-->
	            				</div><!--/gallery-item-expand-->
	            			</div><!--/gallery-item-->

	            			<div class="gallery-item masonry-item col-lg-3 col-md-4 col-sm-6 col-xs-12" data-filter="large medium" data-name="c" data-tags="Officiis, sint, voluptate, quibusdam, eveniet, veniam tempora, large, medium">
	            				<a class="gallery-image" href="#" data-toggle="gallery-expand">
	            					<img class="lazy" data-original="images/dummy/img3.png" alt="Gallery image" />
	            				</a><!--/gallery-image-->

	            				<div class="gallery-caption">
	            					<p>Commodi, cupiditate, obcaecati</p>
	            					<p class="pull-right">
	            						<a href="#"><i class="fa fa-heart"></i> 67</a> &nbsp;&nbsp; <a href="#"><i class="fa fa-comments"></i> 34</a>
	            					</p>
	            				</div><!--/gallery-caption-->

	            				<div class="gallery-item-expand">
	            					<div class="gi-actions btn-group">
	            						<div class="btn-group">
		            						<button href="#" class="btn btn-cloud btn-xs dropdown-toggle" data-toggle="dropdown">
		            							<i class="fa fa-ellipsis-h"></i>
	            							</button>
	            							<ul class="dropdown-menu pull-right" role="menu">
	            								<li><a href="#">Download</a></li>
	            								<li><a href="#">Share</a></li>
	            								<li><a href="#">Edit</a></li>
	            								<li class="divider"></li>
	            								<li><a href="#">Something else</a></li>
	            							</ul>
	            						</div><!--/btn-group-->
	            						<button href="#" class="btn btn-cloud btn-xs hidden-md hidden-lg" data-toggle="gallery-expand-caption"><i class="fa fa-th-large"></i></button>
	            						<button href="#" class="btn btn-cloud btn-xs" data-toggle="gallery-expand-close"><i class="fa fa-times"></i></button>
	            					</div><!--/gallery-actions-->

	            					<a href="#" class="gi-control-right">
	            						<i class="fa fa-angle-right text-64"></i>
	            					</a><!--/gallery-control-right-->

	            					<a href="#" class="gi-control-left">
	            						<i class="fa fa-angle-left text-64"></i>
	            					</a><!--/gallery-control-right-->

	            					<div class="gi-expand-img">
	            						<img class="lazy" data-original="images/dummy/img3.png" alt="Gallery image" />
	            					</div><!--/gallery-expand-image-->

	            					<div class="panel panel-default bg-inverse">
	            						<div class="panel-body">
	            							<div class="profile-line clearfix">
		                                        <img class="img-circle pull-left" src="images/dummy/uifaces19.jpg" alt="uifaces19" width="46px" width="46px" />
		                                        <div class="text-14"><strong>Phillip Morrison</strong></div>
		                                        <div class="text-muted"><small>Upload on Feb 5, 2014</small></div>
		                                    </div><!--/profile-line-->
	            							<p>Text Caption Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sed, pariatur, iusto ex eius delectus odit dolore ducimus accusantium nostrum enim esse beatae nihil rem quam fuga tempore nisi harum cupiditate?</p>
	            						</div><!--/panel-body-->
	            						<ul class="list-group">
                                            <li class="list-group-item">
                                                <div class="pull-right">location/path</div>
                                                Folder
                                            </li>
                                            <li class="list-group-item">
                                                <div class="pull-right">640 x 480</div>
                                                Dimantions
                                            </li>
                                            <li class="list-group-item">
                                                <div class="pull-right">image-name.jpg</div>
                                                File name
                                            </li>
                                            <li class="list-group-item">
                                                <div class="pull-right">16 Kb</div>
                                                File size
                                            </li>
                                            <li class="list-group-item">
                                                <div class="pull-right">Feb 20, 2014</div>
                                                Update
                                            </li>
                                            <li class="list-group-item">
                                                <small><code>http://site.com/path/image-name.jpg</code></small>
                                            </li>
                                        </ul>
	            					</div><!--/panel as details caption-->
	            				</div><!--/gallery-item-expand-->
	            			</div><!--/gallery-item-->

	            			<div class="gallery-item masonry-item col-lg-3 col-md-4 col-sm-6 col-xs-12" data-filter="small" data-name="g" data-tags="Eos, delectus, dolorem, perferendis, sapiente, numquam, hic, small">
	            				<a class="gallery-image" href="#" data-toggle="gallery-expand">
	            					<img class="lazy" data-original="images/dummy/img4.png" alt="Gallery image" />
	            				</a><!--/gallery-image-->

	            				<div class="gallery-caption">
	            					<p>Commodi, cupiditate, obcaecati</p>
	            					<p class="pull-right">
	            						<a href="#"><i class="fa fa-heart"></i> 67</a> &nbsp;&nbsp; <a href="#"><i class="fa fa-comments"></i> 34</a>
	            					</p>
	            				</div><!--/gallery-caption-->

	            				<div class="gallery-item-expand">
	            					<div class="gi-actions btn-group">
	            						<div class="btn-group">
		            						<button href="#" class="btn btn-cloud btn-xs dropdown-toggle" data-toggle="dropdown">
		            							<i class="fa fa-ellipsis-h"></i>
	            							</button>
	            							<ul class="dropdown-menu pull-right" role="menu">
	            								<li><a href="#">Download</a></li>
	            								<li><a href="#">Share</a></li>
	            								<li><a href="#">Edit</a></li>
	            								<li class="divider"></li>
	            								<li><a href="#">Something else</a></li>
	            							</ul>
	            						</div><!--/btn-group-->
	            						<button href="#" class="btn btn-cloud btn-xs hidden-md hidden-lg" data-toggle="gallery-expand-caption"><i class="fa fa-th-large"></i></button>
	            						<button href="#" class="btn btn-cloud btn-xs" data-toggle="gallery-expand-close"><i class="fa fa-times"></i></button>
	            					</div><!--/gallery-actions-->

	            					<a href="#" class="gi-control-right">
	            						<i class="fa fa-angle-right text-64"></i>
	            					</a><!--/gallery-control-right-->

	            					<a href="#" class="gi-control-left">
	            						<i class="fa fa-angle-left text-64"></i>
	            					</a><!--/gallery-control-right-->

	            					<div class="gi-expand-img">
	            						<img class="lazy" data-original="images/dummy/img4.png" alt="Gallery image" />
	            					</div><!--/gallery-expand-image-->

	            					<div class="panel panel-default bg-inverse">
	            						<div class="panel-body">
	            							<div class="profile-line clearfix">
		                                        <img class="img-circle pull-left" src="images/dummy/uifaces3.jpg" alt="uifaces3" width="46px" width="46px" />
		                                        <div class="text-14"><strong>Aaron James</strong></div>
		                                        <div class="text-muted"><small>Upload on Feb 5, 2014</small></div>
		                                    </div><!--/profile-line-->
	            							<p>Text Caption Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sed, pariatur, iusto ex eius delectus odit dolore ducimus accusantium nostrum enim esse beatae nihil rem quam fuga tempore nisi harum cupiditate?</p>
	            						</div><!--/panel-body-->
	            						<ul class="list-group">
                                            <li class="list-group-item">
                                                <div class="pull-right">location/path</div>
                                                Folder
                                            </li>
                                            <li class="list-group-item">
                                                <div class="pull-right">640 x 480</div>
                                                Dimantions
                                            </li>
                                            <li class="list-group-item">
                                                <div class="pull-right">image-name.jpg</div>
                                                File name
                                            </li>
                                            <li class="list-group-item">
                                                <div class="pull-right">16 Kb</div>
                                                File size
                                            </li>
                                            <li class="list-group-item">
                                                <div class="pull-right">Feb 20, 2014</div>
                                                Update
                                            </li>
                                            <li class="list-group-item">
                                                <small><code>http://site.com/path/image-name.jpg</code></small>
                                            </li>
                                        </ul>
	            					</div><!--/panel as details caption-->
	            				</div><!--/gallery-item-expand-->
	            			</div><!--/gallery-item-->

	            			<div class="gallery-item masonry-item col-lg-3 col-md-4 col-sm-6 col-xs-12" data-filter="medium" data-name="e" data-tags="Minus, fugit, quo, incidunt, earum tenetur eaque, medium">
	            				<a class="gallery-image" href="#" data-toggle="gallery-expand">
	            					<img class="lazy" data-original="images/dummy/img5.png" alt="Gallery image" />
	            				</a><!--/gallery-image-->

	            				<div class="gallery-caption">
	            					<p>Commodi, cupiditate, obcaecati</p>
	            					<p class="pull-right">
	            						<a href="#"><i class="fa fa-heart"></i> 67</a> &nbsp;&nbsp; <a href="#"><i class="fa fa-comments"></i> 34</a>
	            					</p>
	            				</div><!--/gallery-caption-->

	            				<div class="gallery-item-expand">
	            					<div class="gi-actions btn-group">
	            						<div class="btn-group">
		            						<button href="#" class="btn btn-cloud btn-xs dropdown-toggle" data-toggle="dropdown">
		            							<i class="fa fa-ellipsis-h"></i>
	            							</button>
	            							<ul class="dropdown-menu pull-right" role="menu">
	            								<li><a href="#">Download</a></li>
	            								<li><a href="#">Share</a></li>
	            								<li><a href="#">Edit</a></li>
	            								<li class="divider"></li>
	            								<li><a href="#">Something else</a></li>
	            							</ul>
	            						</div><!--/btn-group-->
	            						<button href="#" class="btn btn-cloud btn-xs hidden-md hidden-lg" data-toggle="gallery-expand-caption"><i class="fa fa-th-large"></i></button>
	            						<button href="#" class="btn btn-cloud btn-xs" data-toggle="gallery-expand-close"><i class="fa fa-times"></i></button>
	            					</div><!--/gallery-actions-->

	            					<a href="#" class="gi-control-right">
	            						<i class="fa fa-angle-right text-64"></i>
	            					</a><!--/gallery-control-right-->

	            					<a href="#" class="gi-control-left">
	            						<i class="fa fa-angle-left text-64"></i>
	            					</a><!--/gallery-control-right-->

	            					<div class="gi-expand-img">
	            						<img class="lazy" data-original="images/dummy/img5.png" alt="Gallery image" />
	            					</div><!--/gallery-expand-image-->

	            					<div class="panel panel-default bg-inverse">
	            						<div class="panel-body">
	            							<div class="profile-line clearfix">
		                                        <img class="img-circle pull-left" src="images/dummy/uifaces3.jpg" alt="uifaces3" width="46px" width="46px" />
		                                        <div class="text-14"><strong>Aaron James</strong></div>
		                                        <div class="text-muted"><small>Upload on Yesterday - 6:36 AM</small></div>
		                                    </div><!--/profile-line-->
	            							<p>Text Caption Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sed, pariatur, iusto ex eius delectus odit dolore ducimus accusantium nostrum enim esse beatae nihil rem quam fuga tempore nisi harum cupiditate?</p>
	            						</div><!--/panel-body-->
	            						<ul class="list-group">
                                            <li class="list-group-item">
                                                <div class="pull-right">location/path</div>
                                                Folder
                                            </li>
                                            <li class="list-group-item">
                                                <div class="pull-right">640 x 480</div>
                                                Dimantions
                                            </li>
                                            <li class="list-group-item">
                                                <div class="pull-right">image-name.jpg</div>
                                                File name
                                            </li>
                                            <li class="list-group-item">
                                                <div class="pull-right">16 Kb</div>
                                                File size
                                            </li>
                                            <li class="list-group-item">
                                                <div class="pull-right">Feb 20, 2014</div>
                                                Update
                                            </li>
                                            <li class="list-group-item">
                                                <small><code>http://site.com/path/image-name.jpg</code></small>
                                            </li>
                                        </ul>
	            					</div><!--/panel as details caption-->
	            				</div><!--/gallery-item-expand-->
	            			</div><!--/gallery-item-->

	            			<div class="gallery-item masonry-item col-lg-3 col-md-4 col-sm-6 col-xs-12" data-filter="medium" data-name="u" data-tags="Consequatur, dicta, voluptate, minima, recusandae, maxime mollitia, medium">
	            				<a class="gallery-image" href="#" data-toggle="gallery-expand">
	            					<img class="lazy" data-original="images/dummy/img6.png" alt="Gallery image" />
	            				</a><!--/gallery-image-->

	            				<div class="gallery-caption">
	            					<p>Commodi, cupiditate, obcaecati</p>
	            					<p class="pull-right">
	            						<a href="#"><i class="fa fa-heart"></i> 67</a> &nbsp;&nbsp; <a href="#"><i class="fa fa-comments"></i> 34</a>
	            					</p>
	            				</div><!--/gallery-caption-->

	            				<div class="gallery-item-expand">
	            					<div class="gi-actions btn-group">
	            						<div class="btn-group">
		            						<button href="#" class="btn btn-cloud btn-xs dropdown-toggle" data-toggle="dropdown">
		            							<i class="fa fa-ellipsis-h"></i>
	            							</button>
	            							<ul class="dropdown-menu pull-right" role="menu">
	            								<li><a href="#">Download</a></li>
	            								<li><a href="#">Share</a></li>
	            								<li><a href="#">Edit</a></li>
	            								<li class="divider"></li>
	            								<li><a href="#">Something else</a></li>
	            							</ul>
	            						</div><!--/btn-group-->
	            						<button href="#" class="btn btn-cloud btn-xs hidden-md hidden-lg" data-toggle="gallery-expand-caption"><i class="fa fa-th-large"></i></button>
	            						<button href="#" class="btn btn-cloud btn-xs" data-toggle="gallery-expand-close"><i class="fa fa-times"></i></button>
	            					</div><!--/gallery-actions-->

	            					<a href="#" class="gi-control-right">
	            						<i class="fa fa-angle-right text-64"></i>
	            					</a><!--/gallery-control-right-->

	            					<a href="#" class="gi-control-left">
	            						<i class="fa fa-angle-left text-64"></i>
	            					</a><!--/gallery-control-right-->

	            					<div class="gi-expand-img">
	            						<img class="lazy" data-original="images/dummy/img6.png" alt="Gallery image" />
	            					</div><!--/gallery-expand-image-->

	            					<div class="panel panel-default bg-inverse">
	            						<div class="panel-body">
	            							<div class="profile-line clearfix">
		                                        <img class="img-circle pull-left" src="images/dummy/uifaces21.jpg" alt="uifaces21" width="46px" width="46px" />
		                                        <div class="text-14"><strong>John Doe</strong></div>
		                                        <div class="text-muted"><small>Upload on Feb 5, 2014</small></div>
		                                    </div><!--/profile-line-->
	            							<p>Text Caption Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sed, pariatur, iusto ex eius delectus odit dolore ducimus accusantium nostrum enim esse beatae nihil rem quam fuga tempore nisi harum cupiditate?</p>
	            						</div><!--/panel-body-->
	            						<ul class="list-group">
                                            <li class="list-group-item">
                                                <div class="pull-right">location/path</div>
                                                Folder
                                            </li>
                                            <li class="list-group-item">
                                                <div class="pull-right">640 x 480</div>
                                                Dimantions
                                            </li>
                                            <li class="list-group-item">
                                                <div class="pull-right">image-name.jpg</div>
                                                File name
                                            </li>
                                            <li class="list-group-item">
                                                <div class="pull-right">16 Kb</div>
                                                File size
                                            </li>
                                            <li class="list-group-item">
                                                <div class="pull-right">Feb 20, 2014</div>
                                                Update
                                            </li>
                                            <li class="list-group-item">
                                                <small><code>http://site.com/path/image-name.jpg</code></small>
                                            </li>
                                        </ul>
	            					</div><!--/panel as details caption-->
	            				</div><!--/gallery-item-expand-->
	            			</div><!--/gallery-item-->

	            			<div class="gallery-item masonry-item col-lg-3 col-md-4 col-sm-6 col-xs-12" data-filter="medium" data-name="t" data-tags="Nostrum, recusandae, quasi, doloribus, sit, vel repudiandae, medium">
	            				<a class="gallery-image" href="#" data-toggle="gallery-expand">
	            					<img class="lazy" data-original="images/dummy/img7.png" alt="Gallery image" />
	            				</a><!--/gallery-image-->

	            				<div class="gallery-caption">
	            					<p>Commodi, cupiditate, obcaecati</p>
	            					<p class="pull-right">
	            						<a href="#"><i class="fa fa-heart"></i> 67</a> &nbsp;&nbsp; <a href="#"><i class="fa fa-comments"></i> 34</a>
	            					</p>
	            				</div><!--/gallery-caption-->

	            				<div class="gallery-item-expand">
	            					<div class="gi-actions btn-group">
	            						<div class="btn-group">
		            						<button href="#" class="btn btn-cloud btn-xs dropdown-toggle" data-toggle="dropdown">
		            							<i class="fa fa-ellipsis-h"></i>
	            							</button>
	            							<ul class="dropdown-menu pull-right" role="menu">
	            								<li><a href="#">Download</a></li>
	            								<li><a href="#">Share</a></li>
	            								<li><a href="#">Edit</a></li>
	            								<li class="divider"></li>
	            								<li><a href="#">Something else</a></li>
	            							</ul>
	            						</div><!--/btn-group-->
	            						<button href="#" class="btn btn-cloud btn-xs hidden-md hidden-lg" data-toggle="gallery-expand-caption"><i class="fa fa-th-large"></i></button>
	            						<button href="#" class="btn btn-cloud btn-xs" data-toggle="gallery-expand-close"><i class="fa fa-times"></i></button>
	            					</div><!--/gallery-actions-->

	            					<a href="#" class="gi-control-right">
	            						<i class="fa fa-angle-right text-64"></i>
	            					</a><!--/gallery-control-right-->

	            					<a href="#" class="gi-control-left">
	            						<i class="fa fa-angle-left text-64"></i>
	            					</a><!--/gallery-control-right-->

	            					<div class="gi-expand-img">
	            						<img class="lazy" data-original="images/dummy/img7.png" alt="Gallery image" />
	            					</div><!--/gallery-expand-image-->

	            					<div class="panel panel-default bg-inverse">
	            						<div class="panel-body">
	            							<div class="profile-line clearfix">
		                                        <img class="img-circle pull-left" src="images/dummy/uifaces14.jpg" alt="uifaces14" width="46px" width="46px" />
		                                        <div class="text-14"><strong>Kathy Reynolds</strong></div>
		                                        <div class="text-muted"><small>Upload on Feb 5, 2014</small></div>
		                                    </div><!--/profile-line-->
	            							<p>Text Caption Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sed, pariatur, iusto ex eius delectus odit dolore ducimus accusantium nostrum enim esse beatae nihil rem quam fuga tempore nisi harum cupiditate?</p>
	            						</div><!--/panel-body-->
	            						<ul class="list-group">
                                            <li class="list-group-item">
                                                <div class="pull-right">location/path</div>
                                                Folder
                                            </li>
                                            <li class="list-group-item">
                                                <div class="pull-right">640 x 480</div>
                                                Dimantions
                                            </li>
                                            <li class="list-group-item">
                                                <div class="pull-right">image-name.jpg</div>
                                                File name
                                            </li>
                                            <li class="list-group-item">
                                                <div class="pull-right">16 Kb</div>
                                                File size
                                            </li>
                                            <li class="list-group-item">
                                                <div class="pull-right">Feb 20, 2014</div>
                                                Update
                                            </li>
                                            <li class="list-group-item">
                                                <small><code>http://site.com/path/image-name.jpg</code></small>
                                            </li>
                                        </ul>
	            					</div><!--/panel as details caption-->
	            				</div><!--/gallery-item-expand-->
	            			</div><!--/gallery-item-->

	            			<div class="gallery-item masonry-item col-lg-3 col-md-4 col-sm-6 col-xs-12" data-filter="small" data-name="y" data-tags="Ut modi, libero, quam, optio, quisquam culpa, small">
	            				<a class="gallery-image" href="#" data-toggle="gallery-expand">
	            					<img class="lazy" data-original="images/dummy/img9.png" alt="Gallery image" />
	            				</a><!--/gallery-image-->

	            				<div class="gallery-caption">
	            					<p>Commodi, cupiditate, obcaecati</p>
	            					<p class="pull-right">
	            						<a href="#"><i class="fa fa-heart"></i> 67</a> &nbsp;&nbsp; <a href="#"><i class="fa fa-comments"></i> 34</a>
	            					</p>
	            				</div><!--/gallery-caption-->

	            				<div class="gallery-item-expand">
	            					<div class="gi-actions btn-group">
	            						<div class="btn-group">
		            						<button href="#" class="btn btn-cloud btn-xs dropdown-toggle" data-toggle="dropdown">
		            							<i class="fa fa-ellipsis-h"></i>
	            							</button>
	            							<ul class="dropdown-menu pull-right" role="menu">
	            								<li><a href="#">Download</a></li>
	            								<li><a href="#">Share</a></li>
	            								<li><a href="#">Edit</a></li>
	            								<li class="divider"></li>
	            								<li><a href="#">Something else</a></li>
	            							</ul>
	            						</div><!--/btn-group-->
	            						<button href="#" class="btn btn-cloud btn-xs hidden-md hidden-lg" data-toggle="gallery-expand-caption"><i class="fa fa-th-large"></i></button>
	            						<button href="#" class="btn btn-cloud btn-xs" data-toggle="gallery-expand-close"><i class="fa fa-times"></i></button>
	            					</div><!--/gallery-actions-->

	            					<a href="#" class="gi-control-right">
	            						<i class="fa fa-angle-right text-64"></i>
	            					</a><!--/gallery-control-right-->

	            					<a href="#" class="gi-control-left">
	            						<i class="fa fa-angle-left text-64"></i>
	            					</a><!--/gallery-control-right-->

	            					<div class="gi-expand-img">
	            						<img class="lazy" data-original="images/dummy/img9.png" alt="Gallery image" />
	            					</div><!--/gallery-expand-image-->

	            					<div class="panel panel-default bg-inverse">
	            						<div class="panel-body">
	            							<div class="profile-line clearfix">
		                                        <img class="img-circle pull-left" src="images/dummy/uifaces19.jpg" alt="uifaces19" width="46px" width="46px" />
		                                        <div class="text-14"><strong>Phillip Morrison</strong></div>
		                                        <div class="text-muted"><small>Upload on Feb 5, 2014</small></div>
		                                    </div><!--/profile-line-->
	            							<p>Text Caption Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sed, pariatur, iusto ex eius delectus odit dolore ducimus accusantium nostrum enim esse beatae nihil rem quam fuga tempore nisi harum cupiditate?</p>
	            						</div><!--/panel-body-->
	            						<ul class="list-group">
                                            <li class="list-group-item">
                                                <div class="pull-right">location/path</div>
                                                Folder
                                            </li>
                                            <li class="list-group-item">
                                                <div class="pull-right">640 x 480</div>
                                                Dimantions
                                            </li>
                                            <li class="list-group-item">
                                                <div class="pull-right">image-name.jpg</div>
                                                File name
                                            </li>
                                            <li class="list-group-item">
                                                <div class="pull-right">16 Kb</div>
                                                File size
                                            </li>
                                            <li class="list-group-item">
                                                <div class="pull-right">Feb 20, 2014</div>
                                                Update
                                            </li>
                                            <li class="list-group-item">
                                                <small><code>http://site.com/path/image-name.jpg</code></small>
                                            </li>
                                        </ul>
	            					</div><!--/panel as details caption-->
	            				</div><!--/gallery-item-expand-->
	            			</div><!--/gallery-item-->

	            			<div class="gallery-item masonry-item col-lg-6 col-md-8 col-sm-6 col-xs-12" data-filter="large small" data-name="w" data-tags="Nihil, quaerat, nemo, voluptatum, harum, minima dolores, large, small">
	            				<a class="gallery-image" href="#" data-toggle="gallery-expand">
	            					<img class="lazy" data-original="images/dummy/img10.png" alt="Gallery image" />
	            				</a><!--/gallery-image-->

	            				<div class="gallery-caption">
	            					<p>Commodi, cupiditate, obcaecati</p>
	            					<p class="pull-right">
	            						<a href="#"><i class="fa fa-heart"></i> 67</a> &nbsp;&nbsp; <a href="#"><i class="fa fa-comments"></i> 34</a>
	            					</p>
	            				</div><!--/gallery-caption-->



	            				<div class="gallery-item-expand">
	            					<div class="gi-actions btn-group">
	            						<div class="btn-group">
		            						<button href="#" class="btn btn-cloud btn-xs dropdown-toggle" data-toggle="dropdown">
		            							<i class="fa fa-ellipsis-h"></i>
	            							</button>
	            							<ul class="dropdown-menu pull-right" role="menu">
	            								<li><a href="#">Download</a></li>
	            								<li><a href="#">Share</a></li>
	            								<li><a href="#">Edit</a></li>
	            								<li class="divider"></li>
	            								<li><a href="#">Something else</a></li>
	            							</ul>
	            						</div><!--/btn-group-->
	            						<button href="#" class="btn btn-cloud btn-xs hidden-md hidden-lg" data-toggle="gallery-expand-caption"><i class="fa fa-th-large"></i></button>
	            						<button href="#" class="btn btn-cloud btn-xs" data-toggle="gallery-expand-close"><i class="fa fa-times"></i></button>
	            					</div><!--/gallery-actions-->

	            					<a href="#" class="gi-control-right">
	            						<i class="fa fa-angle-right text-64"></i>
	            					</a><!--/gallery-control-right-->

	            					<a href="#" class="gi-control-left">
	            						<i class="fa fa-angle-left text-64"></i>
	            					</a><!--/gallery-control-right-->

	            					<div class="gi-expand-img">
	            						<img class="lazy" data-original="images/dummy/img10.png" alt="Gallery image" />
	            					</div><!--/gallery-expand-image-->

	            					<div class="panel panel-default bg-inverse">
	            						<div class="panel-body">
	            							<div class="profile-line clearfix">
		                                        <img class="img-circle pull-left" src="images/dummy/uifaces19.jpg" alt="uifaces19" width="46px" width="46px" />
		                                        <div class="text-14"><strong>Phillip Morrison</strong></div>
		                                        <div class="text-muted"><small>Upload on Feb 5, 2014</small></div>
		                                    </div><!--/profile-line-->
	            							<p>Text Caption Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sed, pariatur, iusto ex eius delectus odit dolore ducimus accusantium nostrum enim esse beatae nihil rem quam fuga tempore nisi harum cupiditate?</p>
	            						</div><!--/panel-body-->
	            						<ul class="list-group">
                                            <li class="list-group-item">
                                                <div class="pull-right">location/path</div>
                                                Folder
                                            </li>
                                            <li class="list-group-item">
                                                <div class="pull-right">640 x 480</div>
                                                Dimantions
                                            </li>
                                            <li class="list-group-item">
                                                <div class="pull-right">image-name.jpg</div>
                                                File name
                                            </li>
                                            <li class="list-group-item">
                                                <div class="pull-right">16 Kb</div>
                                                File size
                                            </li>
                                            <li class="list-group-item">
                                                <div class="pull-right">Feb 20, 2014</div>
                                                Update
                                            </li>
                                            <li class="list-group-item">
                                                <small><code>http://site.com/path/image-name.jpg</code></small>
                                            </li>
                                        </ul>
	            					</div><!--/panel as details caption-->
	            				</div><!--/gallery-item-expand-->
	            			</div><!--/gallery-item-->

	            			<div class="gallery-item masonry-item col-lg-3 col-md-4 col-sm-6 col-xs-12 h-2x" data-filter="medium" data-name="o" data-tags="Quia, nisi, quam, quas, quod, cumque, voluptatum, medium">
	            				<a class="gallery-image" href="#" data-toggle="gallery-expand">
	            					<img class="lazy" data-original="images/dummy/img8.png" alt="Gallery image" />
	            				</a><!--/gallery-image-->

	            				<div class="gallery-caption">
	            					<p>Commodi, cupiditate, obcaecati</p>
	            					<p class="pull-right">
	            						<a href="#"><i class="fa fa-heart"></i> 67</a> &nbsp;&nbsp; <a href="#"><i class="fa fa-comments"></i> 34</a>
	            					</p>
	            				</div><!--/gallery-caption-->

	            				<div class="gallery-item-expand">
	            					<div class="gi-actions btn-group">
	            						<div class="btn-group">
		            						<button href="#" class="btn btn-cloud btn-xs dropdown-toggle" data-toggle="dropdown">
		            							<i class="fa fa-ellipsis-h"></i>
	            							</button>
	            							<ul class="dropdown-menu pull-right" role="menu">
	            								<li><a href="#">Download</a></li>
	            								<li><a href="#">Share</a></li>
	            								<li><a href="#">Edit</a></li>
	            								<li class="divider"></li>
	            								<li><a href="#">Something else</a></li>
	            							</ul>
	            						</div><!--/btn-group-->
	            						<button href="#" class="btn btn-cloud btn-xs hidden-md hidden-lg" data-toggle="gallery-expand-caption"><i class="fa fa-th-large"></i></button>
	            						<button href="#" class="btn btn-cloud btn-xs" data-toggle="gallery-expand-close"><i class="fa fa-times"></i></button>
	            					</div><!--/gallery-actions-->

	            					<a href="#" class="gi-control-right">
	            						<i class="fa fa-angle-right text-64"></i>
	            					</a><!--/gallery-control-right-->

	            					<a href="#" class="gi-control-left">
	            						<i class="fa fa-angle-left text-64"></i>
	            					</a><!--/gallery-control-right-->

	            					<div class="gi-expand-img">
	            						<img class="lazy" data-original="images/dummy/img8.png" alt="Gallery image" />
	            					</div><!--/gallery-expand-image-->

	            					<div class="panel panel-default bg-inverse">
	            						<div class="panel-body">
	            							<div class="profile-line clearfix">
		                                        <img class="img-circle pull-left" src="images/dummy/uifaces3.jpg" alt="uifaces3" width="46px" width="46px" />
		                                        <div class="text-14"><strong>Aaron James</strong></div>
		                                        <div class="text-muted"><small>Upload on Feb 5, 2014</small></div>
		                                    </div><!--/profile-line-->
	            							<p>Text Caption Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sed, pariatur, iusto ex eius delectus odit dolore ducimus accusantium nostrum enim esse beatae nihil rem quam fuga tempore nisi harum cupiditate?</p>
	            						</div><!--/panel-body-->
	            						<ul class="list-group">
                                            <li class="list-group-item">
                                                <div class="pull-right">location/path</div>
                                                Folder
                                            </li>
                                            <li class="list-group-item">
                                                <div class="pull-right">640 x 480</div>
                                                Dimantions
                                            </li>
                                            <li class="list-group-item">
                                                <div class="pull-right">image-name.jpg</div>
                                                File name
                                            </li>
                                            <li class="list-group-item">
                                                <div class="pull-right">16 Kb</div>
                                                File size
                                            </li>
                                            <li class="list-group-item">
                                                <div class="pull-right">Feb 20, 2014</div>
                                                Update
                                            </li>
                                            <li class="list-group-item">
                                                <small><code>http://site.com/path/image-name.jpg</code></small>
                                            </li>
                                        </ul>
	            					</div><!--/panel as details caption-->
	            				</div><!--/gallery-item-expand-->
	            			</div><!--/gallery-item-->

	            			<div class="gallery-item masonry-item col-lg-3 col-md-4 col-sm-6 col-xs-12" data-filter="large" data-name="f" data-tags="Dolor, mollitia, aliquam, optio, quae, reiciendis, labore, large">
	            				<a class="gallery-image" href="#" data-toggle="gallery-expand">
	            					<img class="lazy" data-original="images/dummy/img2.png" alt="Gallery image" />
	            				</a><!--/gallery-image-->

	            				<div class="gallery-caption">
	            					<p>Commodi, cupiditate, obcaecati</p>
	            					<p class="pull-right">
	            						<a href="#"><i class="fa fa-heart"></i> 67</a> &nbsp;&nbsp; <a href="#"><i class="fa fa-comments"></i> 34</a>
	            					</p>
	            				</div><!--/gallery-caption-->

	            				<div class="gallery-item-expand">
	            					<div class="gi-actions btn-group">
	            						<div class="btn-group">
		            						<button href="#" class="btn btn-cloud btn-xs dropdown-toggle" data-toggle="dropdown">
		            							<i class="fa fa-ellipsis-h"></i>
	            							</button>
	            							<ul class="dropdown-menu pull-right" role="menu">
	            								<li><a href="#">Download</a></li>
	            								<li><a href="#">Share</a></li>
	            								<li><a href="#">Edit</a></li>
	            								<li class="divider"></li>
	            								<li><a href="#">Something else</a></li>
	            							</ul>
	            						</div><!--/btn-group-->
	            						<button href="#" class="btn btn-cloud btn-xs hidden-md hidden-lg" data-toggle="gallery-expand-caption"><i class="fa fa-th-large"></i></button>
	            						<button href="#" class="btn btn-cloud btn-xs" data-toggle="gallery-expand-close"><i class="fa fa-times"></i></button>
	            					</div><!--/gallery-actions-->

	            					<a href="#" class="gi-control-right">
	            						<i class="fa fa-angle-right text-64"></i>
	            					</a><!--/gallery-control-right-->

	            					<a href="#" class="gi-control-left">
	            						<i class="fa fa-angle-left text-64"></i>
	            					</a><!--/gallery-control-right-->

	            					<div class="gi-expand-img">
	            						<img class="lazy" data-original="images/dummy/img2.png" alt="Gallery image" />
	            					</div><!--/gallery-expand-image-->

	            					<div class="panel panel-default bg-inverse">
	            						<div class="panel-body">
	            							<div class="profile-line clearfix">
		                                        <img class="img-circle pull-left" src="images/dummy/uifaces3.jpg" alt="uifaces3" width="46px" width="46px" />
		                                        <div class="text-14"><strong>Aaron James</strong></div>
		                                        <div class="text-muted"><small>Upload on Yesterday - 6:36 AM</small></div>
		                                    </div><!--/profile-line-->
	            							<p>Text Caption Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sed, pariatur, iusto ex eius delectus odit dolore ducimus accusantium nostrum enim esse beatae nihil rem quam fuga tempore nisi harum cupiditate?</p>
	            						</div><!--/panel-body-->
	            						<ul class="list-group">
                                            <li class="list-group-item">
                                                <div class="pull-right">location/path</div>
                                                Folder
                                            </li>
                                            <li class="list-group-item">
                                                <div class="pull-right">640 x 480</div>
                                                Dimantions
                                            </li>
                                            <li class="list-group-item">
                                                <div class="pull-right">image-name.jpg</div>
                                                File name
                                            </li>
                                            <li class="list-group-item">
                                                <div class="pull-right">16 Kb</div>
                                                File size
                                            </li>
                                            <li class="list-group-item">
                                                <div class="pull-right">Feb 20, 2014</div>
                                                Update
                                            </li>
                                            <li class="list-group-item">
                                                <small><code>http://site.com/path/image-name.jpg</code></small>
                                            </li>
                                        </ul>
	            					</div><!--/panel as details caption-->
	            				</div><!--/gallery-item-expand-->
	            			</div><!--/gallery-item-->

	            			<div class="gallery-item masonry-item col-lg-3 col-md-4 col-sm-6 col-xs-12" data-filter="small" data-name="aa" data-tags="Accusantium, doloremque, veritatis, minima, tenetur, unde temporibus, small">
	            				<a class="gallery-image" href="#" data-toggle="gallery-expand">
	            					<img class="lazy" data-original="images/dummy/img4.png" alt="Gallery image" />
	            				</a><!--/gallery-image-->

	            				<div class="gallery-caption">
	            					<p>Commodi, cupiditate, obcaecati</p>
	            					<p class="pull-right">
	            						<a href="#"><i class="fa fa-heart"></i> 67</a> &nbsp;&nbsp; <a href="#"><i class="fa fa-comments"></i> 34</a>
	            					</p>
	            				</div><!--/gallery-caption-->

	            				<div class="gallery-item-expand">
	            					<div class="gi-actions btn-group">
	            						<div class="btn-group">
		            						<button href="#" class="btn btn-cloud btn-xs dropdown-toggle" data-toggle="dropdown">
		            							<i class="fa fa-ellipsis-h"></i>
	            							</button>
	            							<ul class="dropdown-menu pull-right" role="menu">
	            								<li><a href="#">Download</a></li>
	            								<li><a href="#">Share</a></li>
	            								<li><a href="#">Edit</a></li>
	            								<li class="divider"></li>
	            								<li><a href="#">Something else</a></li>
	            							</ul>
	            						</div><!--/btn-group-->
	            						<button href="#" class="btn btn-cloud btn-xs hidden-md hidden-lg" data-toggle="gallery-expand-caption"><i class="fa fa-th-large"></i></button>
	            						<button href="#" class="btn btn-cloud btn-xs" data-toggle="gallery-expand-close"><i class="fa fa-times"></i></button>
	            					</div><!--/gallery-actions-->

	            					<a href="#" class="gi-control-right">
	            						<i class="fa fa-angle-right text-64"></i>
	            					</a><!--/gallery-control-right-->

	            					<a href="#" class="gi-control-left">
	            						<i class="fa fa-angle-left text-64"></i>
	            					</a><!--/gallery-control-right-->

	            					<div class="gi-expand-img">
	            						<img class="lazy" data-original="images/dummy/img4.png" alt="Gallery image" />
	            					</div><!--/gallery-expand-image-->

	            					<div class="panel panel-default bg-inverse">
	            						<div class="panel-body">
	            							<div class="profile-line clearfix">
		                                        <img class="img-circle pull-left" src="images/dummy/uifaces21.jpg" alt="uifaces21" width="46px" width="46px" />
		                                        <div class="text-14"><strong>John Doe</strong></div>
		                                        <div class="text-muted"><small>Upload on Feb 5, 2014</small></div>
		                                    </div><!--/profile-line-->
	            							<p>Text Caption Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sed, pariatur, iusto ex eius delectus odit dolore ducimus accusantium nostrum enim esse beatae nihil rem quam fuga tempore nisi harum cupiditate?</p>
	            						</div><!--/panel-body-->
	            						<ul class="list-group">
                                            <li class="list-group-item">
                                                <div class="pull-right">location/path</div>
                                                Folder
                                            </li>
                                            <li class="list-group-item">
                                                <div class="pull-right">640 x 480</div>
                                                Dimantions
                                            </li>
                                            <li class="list-group-item">
                                                <div class="pull-right">image-name.jpg</div>
                                                File name
                                            </li>
                                            <li class="list-group-item">
                                                <div class="pull-right">16 Kb</div>
                                                File size
                                            </li>
                                            <li class="list-group-item">
                                                <div class="pull-right">Feb 20, 2014</div>
                                                Update
                                            </li>
                                            <li class="list-group-item">
                                                <small><code>http://site.com/path/image-name.jpg</code></small>
                                            </li>
                                        </ul>
	            					</div><!--/panel as details caption-->
	            				</div><!--/gallery-item-expand-->
	            			</div><!--/gallery-item-->

	            			<div class="gallery-item masonry-item col-lg-3 col-md-4 col-sm-6 col-xs-12" data-filter="medium" data-name="dd" data-tags="Ipsa, accusamus, magni, ipsum, nemo, enim cupiditate, medium">
	            				<a class="gallery-image" href="#" data-toggle="gallery-expand">
	            					<img class="lazy" data-original="images/dummy/img6.png" alt="Gallery image" />
	            				</a><!--/gallery-image-->

	            				<div class="gallery-caption">
	            					<p>Commodi, cupiditate, obcaecati</p>
	            					<p class="pull-right">
	            						<a href="#"><i class="fa fa-heart"></i> 67</a> &nbsp;&nbsp; <a href="#"><i class="fa fa-comments"></i> 34</a>
	            					</p>
	            				</div><!--/gallery-caption-->

	            				<div class="gallery-item-expand">
	            					<div class="gi-actions btn-group">
	            						<div class="btn-group">
		            						<button href="#" class="btn btn-cloud btn-xs dropdown-toggle" data-toggle="dropdown">
		            							<i class="fa fa-ellipsis-h"></i>
	            							</button>
	            							<ul class="dropdown-menu pull-right" role="menu">
	            								<li><a href="#">Download</a></li>
	            								<li><a href="#">Share</a></li>
	            								<li><a href="#">Edit</a></li>
	            								<li class="divider"></li>
	            								<li><a href="#">Something else</a></li>
	            							</ul>
	            						</div><!--/btn-group-->
	            						<button href="#" class="btn btn-cloud btn-xs hidden-md hidden-lg" data-toggle="gallery-expand-caption"><i class="fa fa-th-large"></i></button>
	            						<button href="#" class="btn btn-cloud btn-xs" data-toggle="gallery-expand-close"><i class="fa fa-times"></i></button>
	            					</div><!--/gallery-actions-->

	            					<a href="#" class="gi-control-right">
	            						<i class="fa fa-angle-right text-64"></i>
	            					</a><!--/gallery-control-right-->

	            					<a href="#" class="gi-control-left">
	            						<i class="fa fa-angle-left text-64"></i>
	            					</a><!--/gallery-control-right-->

	            					<div class="gi-expand-img">
	            						<img class="lazy" data-original="images/dummy/img6.png" alt="Gallery image" />
	            					</div><!--/gallery-expand-image-->

	            					<div class="panel panel-default bg-inverse">
	            						<div class="panel-body">
	            							<div class="profile-line clearfix">
		                                        <img class="img-circle pull-left" src="images/dummy/uifaces14.jpg" alt="uifaces14" width="46px" width="46px" />
		                                        <div class="text-14"><strong>Kathy Reynolds</strong></div>
		                                        <div class="text-muted"><small>Upload on Feb 5, 2014</small></div>
		                                    </div><!--/profile-line-->
	            							<p>Text Caption Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sed, pariatur, iusto ex eius delectus odit dolore ducimus accusantium nostrum enim esse beatae nihil rem quam fuga tempore nisi harum cupiditate?</p>
	            						</div><!--/panel-body-->
	            						<ul class="list-group">
                                            <li class="list-group-item">
                                                <div class="pull-right">location/path</div>
                                                Folder
                                            </li>
                                            <li class="list-group-item">
                                                <div class="pull-right">640 x 480</div>
                                                Dimantions
                                            </li>
                                            <li class="list-group-item">
                                                <div class="pull-right">image-name.jpg</div>
                                                File name
                                            </li>
                                            <li class="list-group-item">
                                                <div class="pull-right">16 Kb</div>
                                                File size
                                            </li>
                                            <li class="list-group-item">
                                                <div class="pull-right">Feb 20, 2014</div>
                                                Update
                                            </li>
                                            <li class="list-group-item">
                                                <small><code>http://site.com/path/image-name.jpg</code></small>
                                            </li>
                                        </ul>
	            					</div><!--/panel as details caption-->
	            				</div><!--/gallery-item-expand-->
	            			</div><!--/gallery-item-->

	                    </div><!--/gallery-wrapper-->
                    </div><!--/container-->


                    <p class="text-center">
        				<a href="#" class="btn btn-cloud btn-sm">Load more images...</a>
        			</p>