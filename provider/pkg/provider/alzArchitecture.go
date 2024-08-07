// Copyright 2016-2021, Pulumi Corporation.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package provider

import (
	"github.com/pulumi/pulumi-azure-native-sdk/management/v2"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The set of arguments for creating a StaticPage component resource.
type AlzArchitectureArgs struct {
	ArchitectureName      pulumi.StringInput `pulumi:"architectureName"`      // The name of the ALZ architecture from the library.
	Location              pulumi.StringInput `pulumi:"location"`              // The default location for resources.
	RootManagementGroupId pulumi.StringInput `pulumi:"rootManagementGroupId"` // The root management group ID.
}

// The AlzArchitecture component resource.
type AlzArchitecture struct {
	pulumi.ResourceState

	ManagementGroups []management.ManagementGroup `pulumi:"managementGroups"`
}

// NewStaticPage creates a new StaticPage component resource.
func NewStaticPage(ctx *pulumi.Context,
	name string, args *AlzArchitectureArgs, opts ...pulumi.ResourceOption) (*AlzArchitecture, error) {
	if args == nil {
		args = &AlzArchitectureArgs{}
	}

	component := &AlzArchitecture{}
	err := ctx.RegisterComponentResource("azure:index:StaticPage", name, component, opts...)
	if err != nil {
		return nil, err
	}

	// // Create a bucket and expose a website index document.
	// bucket, err := s3.NewBucket(ctx, name, &s3.BucketArgs{
	// 	Website: s3.BucketWebsiteArgs{
	// 		IndexDocument: pulumi.String("index.html"),
	// 	},
	// }, pulumi.Parent(component))
	// if err != nil {
	// 	return nil, err
	// }

	// // Create a bucket object for the index document.
	// if _, err := s3.NewBucketObject(ctx, name, &s3.BucketObjectArgs{
	// 	Bucket:      bucket.ID(),
	// 	Key:         pulumi.String("index.html"),
	// 	Content:     args.IndexContent,
	// 	ContentType: pulumi.String("text/html"),
	// }, pulumi.Parent(bucket)); err != nil {
	// 	return nil, err
	// }

	// Set the access policy for the bucket so all objects are readable.
	// if _, err := s3.NewBucketPolicy(ctx, "bucketPolicy", &s3.BucketPolicyArgs{
	// 	Bucket: bucket.ID(),
	// 	Policy: pulumi.Any(map[string]interface{}{
	// 		"Version": "2012-10-17",
	// 		"Statement": []map[string]interface{}{
	// 			{
	// 				"Effect":    "Allow",
	// 				"Principal": "*",
	// 				"Action": []interface{}{
	// 					"s3:GetObject",
	// 				},
	// 				"Resource": []interface{}{
	// 					pulumi.Sprintf("arn:aws:s3:::%s/*", bucket.ID()), // policy refers to bucket name explicitly
	// 				},
	// 			},
	// 		},
	// 	}),
	// }, pulumi.Parent(bucket)); err != nil {
	// 	return nil, err
	// }

	// component.Bucket = bucket
	// component.WebsiteUrl = bucket.WebsiteEndpoint

	// if err := ctx.RegisterResourceOutputs(component, pulumi.Map{
	// 	"bucket":     bucket,
	// 	"websiteUrl": bucket.WebsiteEndpoint,
	// }); err != nil {
	// 	return nil, err
	// }

	return component, nil
}
