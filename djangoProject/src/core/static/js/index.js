
  
  $('#pagination-long').materializePagination({
      align: 'center',
      lastPage:  2000,
      firstPage:  1,
      useUrlParameter: false,
      onClickCallback: function(requestedPage){
          console.log('Requested page from #pagination-long: '+ requestedPage);
      }
  }); 