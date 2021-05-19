This is implementation of a simple audio file server simulator using Django Rest Framework

With Implemented create, read, upload, and delete(CRUD) endpoints for an audio file as defined below:  
1. Create API: 
    The request will have the following fields: - audioFileType – mandatory, one of the 3 audio types possible - audioFileMetadata – mandatory, dictionary, contains the metadata for one of the three audio files (song, podcast, audiobook) 
    
    else:- you can directly use the link for audio file type and post the data for same. 

2. Delete API: 
    The route will be in the following format: “<audioFileType>/<audioFileID>”  

3. Update API: 
     The route be in the following format: “<audioFileType>/<audioFileID>” - The request body will be the same as the upload  

4. Get API: 
    The route “<audioFileType>/<audioFileID>” will return the specific audio file - The route “<audioFileType>” will return all the audio files of that type 