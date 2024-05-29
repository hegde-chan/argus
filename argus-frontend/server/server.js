const AWS = require("aws-sdk")

const dynamodb = new AWS.DynamoDB({ apiVersion: "2012-08-10" });

const main = async () => {
    var params = {
        TableName: "ArgusJobProgressTable",
        Key: {
            jobID: { S: "abcdefg-uuid" },
        },
    };
    dynamodb.getItem(params, function(err)
}

main();