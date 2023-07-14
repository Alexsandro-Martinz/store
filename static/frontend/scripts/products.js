function cleanModalValue(){
    document.getElementById('categoryName').value = '';
}


function deleteProduct(productId) {
    elementName = "product" + productId;
    if (confirm("Delete product?")) {
      $.ajax({
        type: "POST",
        url: "{% url 'frontend:delProduct' %}",
        data: {
          id: productId,
          csrfmiddlewaretoken: "{{ csrf_token }}",
        },
        success: function (response) {
          alert(response["messageSuccess"]);
          document.getElementById(elementName).remove();
        },
        error: function (response) {
          alert(response["responserJSOM"]["error"]);
        },
      });
    }
  }