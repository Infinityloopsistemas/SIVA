<?php

if(!isset($_SERVER['HTTP_X_PJAX'])){

    $content = basename($_SERVER['SCRIPT_NAME']);

    $_SERVER['HTTP_X_PJAX'] = true;
    include 'stilearn.base.template.php';
    die();
}

?>
                    <!-- MAPS
                    ====================== -->
                    <!-- VMAP -->
            		<div class="panel panel-default">
            			<div class="panel-heading bg-white">
                            <div class="panel-actions">
                                <div class="btn-group">
                                    <button class="btn-panel dropdown-toggle" data-toggle="dropdown">
                                        Change Maps
                                        <i class="fa fa-angle-down"></i>
                                    </button>
                                    <ul id="changeMapRegion" class="dropdown-menu pull-right">
                                        <li class="active"><a href="#" data-map="world_en">World</a></li>
                                        <li class="divider"></li>
                                        <li><a href="#" data-map="africa_en">Africa</a></li>
                                        <li><a href="#" data-map="asia_en">Asia</a></li>
                                        <li><a href="#" data-map="australia_en">Australia</a></li>
                                        <li><a href="#" data-map="europe_en">Europe</a></li>
                                        <li><a href="#" data-map="north-america_en">North America</a></li>
                                        <li><a href="#" data-map="south-america_en">South America</a></li>
                                        <li class="divider"></li>
                                        <li><a href="#" data-map="dz_fr">Algeria</a></li>
                                        <li><a href="#" data-map="france_fr">France</a></li>
                                        <li><a href="#" data-map="germany_en">Germany</a></li>
                                        <li><a href="#" data-map="russia_en">Russia</a></li>
                                        <li><a href="#" data-map="usa_en">USA</a></li>
                                    </ul>
                                </div><!--/btn-group-->
                            </div><!-- /panel-actions -->
            				<h4 class="panel-title" data-ariginal-title="World Map" id="mapRegion">World Map</h4>
            			</div><!--panel-heading-->

            			<div class="panel-body">
                        	<div id="vmap" class="vmap"></div>
            			</div><!--panel-body-->
                        
                        <ul class="map-legend list-group">
                            <li class="list-group-item" id="legend-region">Summary of World</li>
                            <li class="list-group-item text-11"><div id="legend-visit" class="badge badge-primary"></div><i class="fa fa-signal"></i> Today Visitor</li>
                            <li class="list-group-item text-11"><div id="legend-member" class="badge badge-primary"></div><i class="fa fa-users"></i> Members</li>
                            <li class="list-group-item text-11"><div id="legend-customer" class="badge badge-primary"></div><i class="fa fa-briefcase"></i> Customers</li>
                            <li class="list-group-item text-11"><div id="legend-online" class="badge badge-primary"></div><i class="fa fa-circle"></i> Online</li>
                            <li class="list-group-item text-11"><div id="legend-revenue" class="badge badge-primary"></div><i class="fa fa-dollar"></i> Total Revenue</li>
                        </ul><!--/list-group map-legend-->
            		</div><!--panel-->



                    <div class="panel panel-inverse">
                        <div class="panel-heading bg-darknight">
                            <h4 class="panel-title">Optional Style</h4>
                        </div><!--panel-heading-->

                        <div class="panel-body bg-darknight">
                            <div id="vmap-inverse" class="vmap"></div>
                        </div><!--panel-body-->
                    </div><!--panel-->
