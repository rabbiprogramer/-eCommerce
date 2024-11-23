<form method="POST" enctype="multipart/form-data">
    {% csrf_token %}
    <div class="row">
        <div class="col-12">
            <div class="card">
                <div class="card-body">
                    <div class="mb-4">
                        <div class="mb-3 row">
                            <div class="col-md-6">
                                <!-- Category -->
                                <div class="form-group">
                                    <label for="{{ form.category.id_for_label }}">Category</label>
                                    {{ form.category }}
                                </div>
                            </div>
                            <div class="col-md-6">
                                <!-- Brand -->
                                <div class="form-group">
                                    <label for="{{ form.brand.id_for_label }}">Brand</label>
                                    {{ form.brand }}
                                </div>
                            </div>
                        </div>

                        <!-- Title -->
                        <div class="form-group mb-3">
                            <label for="{{ form.title.id_for_label }}">Title</label>
                            {{ form.title }}
                        </div>

                        <!-- Description -->
                        <div class="form-group mb-3">
                            <label for="{{ form.description.id_for_label }}">Description</label>
                            {{ form.description }}
                        </div>

                        <!-- Price -->
                        <div class="form-group mb-3">
                            <label for="{{ form.price.id_for_label }}">Price</label>
                            {{ form.price }}
                        </div>

                        <!-- Sale Price -->
                        <div class="form-group mb-3">
                            <label for="{{ form.sale_price.id_for_label }}">Sale Price</label>
                            {{ form.sale_price }}
                        </div>

                        <!-- Regular Price -->
                        <div class="form-group mb-3">
                            <label for="{{ form.regular_price.id_for_label }}">Regular Price</label>
                            {{ form.regular_price }}
                        </div>

                        <!-- Stock -->
                        <div class="form-group mb-3">
                            <label for="{{ form.add_stock.id_for_label }}">Add Stock</label>
                            {{ form.add_stock }}
                        </div>

                        <!-- Restock Quantity -->
                        <div class="form-group mb-3">
                            <label for="{{ form.restock_quantity.id_for_label }}">Restock Quantity</label>
                            {{ form.restock_quantity }}
                        </div>

                        <!-- Shipping Fee -->
                        <div class="form-group mb-3">
                            <label for="{{ form.shipping_fee.id_for_label }}">Shipping Fee</label>
                            {{ form.shipping_fee }}
                        </div>

                        <!-- Global Delivery -->
                        <div class="form-group mb-3">
                            <label for="{{ form.global_delivery.id_for_label }}">Global Delivery</label>
                            {{ form.global_delivery }}
                        </div>

                        <!-- Selected Countries -->
                        <div class="form-group mb-3">
                            <label for="{{ form.selected_countries.id_for_label }}">Selected Countries</label>
                            {{ form.selected_countries }}
                        </div>

                        <!-- Tags -->
                        <div class="form-group mb-3">
                            <label for="{{ form.tags.id_for_label }}">Tags</label>
                            {{ form.tags }}
                        </div>

                        <!-- Collections -->
                        <div class="form-group mb-3">
                            <label for="{{ form.collections.id_for_label }}">Collections</label>
                            {{ form.collections }}
                        </div>

                        <!-- Images -->
                        <div class="form-group mb-3">
                            <label for="{{ form.images.id_for_label }}">Images</label>
                            {{ form.images }}
                        </div>

                        <!-- Attributes -->
                        <div class="form-group mb-3">
                            <label for="{{ form.attributes.id_for_label }}">Attributes</label>
                            {{ form.attributes }}
                        </div>

                        <!-- Shipping Method -->
                        <div class="form-group mb-3">
                            <label for="{{ form.shipping_method.id_for_label }}">Shipping Method</label>
                            <div class="form-check">
                                {{ form.shipping_method }}
                            </div>
                        </div>

                        <!-- Is Fragile -->
                        <div class="form-group mb-3">
                            <label for="{{ form.is_fragile.id_for_label }}">Is Fragile?</label>
                            <div class="form-check">
                                {{ form.is_fragile }}
                            </div>
                        </div>

                        <!-- Is Biodegradable -->
                        <div class="form-group mb-3">
                            <label for="{{ form.is_biodegradable.id_for_label }}">Is Biodegradable?</label>
                            <div class="form-check">
                                {{ form.is_biodegradable }}
                            </div>
                        </div>

                        <!-- SKU -->
                        <div class="form-group mb-3">
                            <label for="{{ form.sku.id_for_label }}">SKU</label>
                            {{ form.sku }}
                        </div>

                        <!-- Color -->
                        <div class="form-group mb-3">
                            <label for="{{ form.color.id_for_label }}">Color</label>
                            {{ form.color }}
                        </div>

                        <!-- Size -->
                        <div class="form-group mb-3">
                            <label for="{{ form.size.id_for_label }}">Size</label>
                            {{ form.size }}
                        </div>

                        <!-- Expiry Date -->
                        <div class="form-group mb-3">
                            <label for="{{ form.expiry_date.id_for_label }}">Expiry Date</label>
                            {{ form.expiry_date }}
                        </div>

                        <!-- Product ID Type -->
                        <div class="form-group mb-3">
                            <label for="{{ form.product_id_type.id_for_label }}">Product ID Type</label>
                            {{ form.product_id_type }}
                        </div>

                        <!-- Product ID -->
                        <div class="form-group mb-3">
                            <label for="{{ form.product_id.id_for_label }}">Product ID</label>
                            {{ form.product_id }}
                        </div>

                        <!-- Submit Button -->
                        <button type="submit" class="btn btn-primary">Add Product</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</form>
