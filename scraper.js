// include the module 
var govTrack = require('govtrack-node');
 
var args = process.argv.slice(2);

jsonArr = []

govTrack.findRole({current : 'true'}, function(err, res){
	if (!err){

		for (x of res.objects){
			// console.log(x.person.firstname)
			// console.log(x)
			jsonArr.push({
				firstname : x.person.firstname,
				lastname : x.person.lastname,
				party : x.party,
				description : x.description,
				title : x.title_long,
				state : x.state,
				birthday : x.person.birthday,
				twitter : x.person.twitterid,
				youtube : x.person.youtubeid,
				leadership : x.leadership_title,
				start_date : x.startdate,
				website : x.website,
			})
		}
		console.log(jsonArr)
	}
	else{
		console.log(err)
	}
});


// govTrack.findPerson({}, function(err, res){
// 	if (!err){
// 		for (x of res.objects){
// 			console.log(x.firstname)
// 			govTrack.findPerson({sortname: x.sortname},function(err,res1){
// 				// console.log(res1.roles[res1.roles.length-1])
// 				jsonArr.push({
// 					firstname : x.firstname,
// 					lastname : x.lastname
// 				})
// 			})
			
// 		}
// 		console.log(jsonArr)
// 	}
// 	else{
// 		console.log(err)
// 	}
// });

// govTrack.findPerson({sortname: "Price, David (Rep.) [D-NC4]"}, function(err, res){
	
// 	if(!err){		
// 		console.log(res)
// 	}
// 	else{
// 		console.log(err)
// 	}
// });


// list current members of Congress 
// govTrack.findRole({current : 'true'}, function(err, res) {
//   if (!err) {
//   	// console.log(res);
//   	// console.log(res.objects[0]);
//   	// console.log("_______________________");

//   	// for (x of res.objects)
//   	// {
//   	// 	console.log(x);
//   	// }
//   	// console.log(res);
//   	for (x of res.objects){
//   		// if(x.person.lastname == 'Reid')
//   		if(x.person.lastname == args[0])
//   		{
//   			console.log(x)
//   			// console.log(x.person.lastname)
  			
//   		}
//   	}
//     // console.log(res);
//   }
// });
 
// console.log("_______________________");

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