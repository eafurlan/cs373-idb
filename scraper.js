// include the module 
var govTrack = require('govtrack-node');
 
var args = process.argv.slice(2);

// list current members of Congress 
govTrack.findRole({current : 'true'}, function(err, res) {
  if (!err) {
  	// console.log(res);
  	// console.log(res.objects[0]);
  	// console.log("_______________________");

  	// for (x of res.objects)
  	// {
  	// 	console.log(x);
  	// }
  	// console.log(res);
  	for (x of res.objects){
  		// if(x.person.lastname == 'Reid')
  		if(x.person.lastname == args[0])
  		{
  			console.log(x)
  			// console.log(x.person.lastname)
  			
  		}
  	}
    // console.log(res);
  }
});
 
console.log("_______________________");

// govTrack.findPerson({}, function(err, res) {
//   if (!err) {
//   	// console.log(res);
//   	// console.log(res.objects);
//   	// console.log(res.objects[0].lastname);
//   	// if(res.person.lastname == 'Aderholt')
//    //  // res contains JSON data response 
//    //  console.log("Found Aderholt!\n");
//    for (x of res.objects){
//    		// console.log(x.lastname)
//    		if(x.lastname == 'Snowe'){
// 	   	  console.log(x)
// 	   	}
//    }
//   }
//   else {
//   	console.log(err);
//   }
// });