from datetime import datetime
import pytz
from .request_data import send_request

def search_agoda(idHotel, start_date, end_date):
    
    # Parse the input string as UTC time
    start_date_local = datetime.strptime(start_date, "%Y-%m-%dT%H:%M:%S.%fZ").replace(tzinfo=pytz.UTC)
    end_date_local = datetime.strptime(end_date, "%Y-%m-%dT%H:%M:%S.%fZ").replace(tzinfo=pytz.UTC)


    # Convert UTC time to Jakarta time
    jakarta_timezone = pytz.timezone('Asia/Jakarta')
    start_date_jakarta = start_date_local.astimezone(jakarta_timezone)
    end_date_jakarta = end_date_local.astimezone(jakarta_timezone)


    # Extract the date part and format as a new string
    start_date_locale = start_date_jakarta.strftime("%Y-%m-%d")
    end_date_locale = end_date_jakarta.strftime("%Y-%m-%d")


    query = """
    query citySearch($CitySearchRequest: CitySearchRequest!, $ContentSummaryRequest: ContentSummaryRequest!, $PricingSummaryRequest: PricingRequestParameters, $PriceStreamMetaLabRequest: PriceStreamMetaLabRequest) {
  citySearch(CitySearchRequest: $CitySearchRequest) {
    featuredPulseProperties(ContentSummaryRequest: $ContentSummaryRequest, PricingSummaryRequest: $PricingSummaryRequest) {
      propertyId
      propertyResultType
      pricing {
        pulseCampaignMetadata {
          promotionTypeId
          webCampaignId
          campaignTypeId
          campaignBadgeText
          campaignBadgeDescText
          dealExpiryTime
          showPulseMerchandise
        }
        isAvailable
        isReady
        offers {
          roomOffers {
            room {
              pricing {
                currency
                price {
                  perNight {
                    exclusive {
                      crossedOutPrice
                      display
                    }
                    inclusive {
                      crossedOutPrice
                      display
                    }
                  }
                  perRoomPerNight {
                    exclusive {
                      crossedOutPrice
                      display
                    }
                    inclusive {
                      crossedOutPrice
                      display
                    }
                  }
                }
              }
            }
          }
        }
      }
      content {
        reviews {
          contentReview {
            isDefault
            providerId
            cumulative {
              reviewCount
              score
            }
          }
          cumulative {
            reviewCount
            score
          }
        }
        images {
          hotelImages {
            urls {
              value
            }
          }
        }
        informationSummary {
          hasHostExperience
          displayName
          rating
          propertyLinks {
            propertyPage
          }
          address {
            country {
              id
            }
            area {
              name
            }
            city {
              name
            }
          }
          nhaSummary {
            hostType
          }
        }
      }
    }
    searchResult {
      sortMatrix {
        result {
          fieldId
          sorting {
            sortField
            sortOrder
            sortParams {
              id
            }
          }
          display {
            name
          }
          childMatrix {
            fieldId
            sorting {
              sortField
              sortOrder
              sortParams {
                id
              }
            }
            display {
              name
            }
            childMatrix {
              fieldId
              sorting {
                sortField
                sortOrder
                sortParams {
                  id
                }
              }
              display {
                name
              }
            }
          }
        }
      }
      searchInfo {
        flexibleSearch {
          currentDate {
            checkIn
            price
          }
          alternativeDates {
            checkIn
            price
          }
        }
        hasSecretDeal
        isComplete
        totalFilteredHotels
        hasEscapesPackage
        searchStatus {
          searchCriteria {
            checkIn
          }
          searchStatus
        }
        objectInfo {
          objectName
          cityName
          cityEnglishName
          countryId
          countryEnglishName
          mapLatitude
          mapLongitude
          mapZoomLevel
          wlPreferredCityName
          wlPreferredCountryName
          cityId
          cityCenterPolygon {
            geoPoints {
              lon
              lat
            }
            touristAreaCenterPoint {
              lon
              lat
            }
          }
        }
      }
      urgencyDetail {
        urgencyScore
      }
      histogram {
        bins {
          numOfElements
          upperBound {
            perNightPerRoom
            perPax
          }
        }
      }
      nhaProbability
    }
    properties(ContentSummaryRequest: $ContentSummaryRequest, PricingSummaryRequest: $PricingSummaryRequest, PriceStreamMetaLabRequest: $PriceStreamMetaLabRequest) {
      propertyId
      sponsoredDetail {
        sponsoredType
        trackingData
        isShowSponsoredFlag
      }
      propertyResultType
      content {
        informationSummary {
          hotelCharacter {
            hotelTag {
              name
              symbol
            }
            hotelView {
              name
              symbol
            }
          }
          propertyLinks {
            propertyPage
          }
          atmospheres {
            id
            name
          }
          isSustainableTravel
          localeName
          defaultName
          displayName
          accommodationType
          awardYear
          hasHostExperience
          nhaSummary {
            isProfessionallyManaged
            hostPropertyCount
          }
          address {
            countryCode
            country {
              id
              name
            }
            city {
              id
              name
            }
            area {
              id
              name
            }
          }
          propertyType
          rating
          agodaGuaranteeProgram
          remarks {
            renovationInfo {
              renovationType
              year
            }
          }
          spokenLanguages {
            id
          }
          geoInfo {
            latitude
            longitude
          }
        }
        propertyEngagement {
          lastBooking
          peopleLooking
        }
        nonHotelAccommodation {
          masterRooms {
            noOfBathrooms
            noOfBedrooms
            noOfBeds
            roomSizeSqm
            highlightedFacilities
          }
          hostLevel {
            id
            name
          }
          supportedLongStay
        }
        facilities {
          id
        }
        images {
          hotelImages {
            id
            caption
            providerId
            urls {
              key
              value
            }
          }
        }
        reviews {
          contentReview {
            isDefault
            providerId
            demographics {
              groups {
                id
                grades {
                  id
                  score
                }
              }
            }
            summaries {
              recommendationScores {
                recommendationScore
              }
              snippets {
                countryId
                countryCode
                countryName
                date
                demographicId
                demographicName
                reviewer
                reviewRating
                snippet
              }
            }
            cumulative {
              reviewCount
              score
            }
          }
          cumulative {
            reviewCount
            score
          }
          cumulativeForHost {
            hostAvgHotelReviewRating
            hostHotelReviewTotalCount
          }
        }
        familyFeatures {
          hasChildrenFreePolicy
          isFamilyRoom
          hasMoreThanOneBedroom
          isInterConnectingRoom
          isInfantCottageAvailable
          hasKidsPool
          hasKidsClub
        }
        personalizedInformation {
          childrenFreePolicy {
            fromAge
            toAge
          }
        }
        localInformation {
          landmarks {
            transportation {
              landmarkName
              distanceInM
            }
            topLandmark {
              landmarkName
              distanceInM
            }
            beach {
              landmarkName
              distanceInM
            }
          }
          hasAirportTransfer
        }
        highlight {
          cityCenter {
            distanceFromCityCenter
          }
          favoriteFeatures {
            features {
              id
              title
              category
            }
          }
          hasNearbyPublicTransportation
        }
        rateCategories {
          escapeRateCategories {
            rateCategoryId
            localizedRateCategoryName
          }
        }
      }
      soldOut {
        soldOutPrice {
          averagePrice
        }
      }
      pricing {
        pulseCampaignMetadata {
          promotionTypeId
          webCampaignId
          campaignTypeId
          campaignBadgeText
          campaignBadgeDescText
          dealExpiryTime
          showPulseMerchandise
        }
        isAvailable
        isReady
        benefits
        cheapestRoomOffer {
          agodaCash {
            showBadge
            giftcardGuid
            dayToEarn
            earnId
            percentage
            expiryDay
          }
          cashback {
            cashbackGuid
            showPostCashbackPrice
            cashbackVersion
            percentage
            earnId
            dayToEarn
            expiryDay
            cashbackType
            appliedCampaignName
          }
        }
        isEasyCancel
        isInsiderDeal
        isMultiHotelEligible
        suggestPriceType {
          suggestPrice
        }
        roomBundle {
          bundleId
          bundleType
          saveAmount {
            perNight {
              ...Fraga0abi1adjdee6711egi6
            }
          }
        }
        pointmax {
          channelId
          point
        }
        priceChange {
          changePercentage
          searchDate
        }
        payment {
          cancellation {
            cancellationType
            freeCancellationDate
          }
          payLater {
            isEligible
          }
          payAtHotel {
            isEligible
          }
          noCreditCard {
            isEligible
          }
          taxReceipt {
            isEligible
          }
        }
        cheapestStayPackageRatePlans {
          stayPackageType
          ratePlanId
        }
        pricingMessages {
          location
          ids
        }
        suppliersSummaries {
          id
          supplierHotelId
        }
        supplierInfo {
          id
          name
          isAgodaBand
        }
        offers {
          roomOffers {
            room {
              extraPriceInfo {
                displayPriceWithSurchargesPRPN
                corDisplayPriceWithSurchargesPRPN
              }
              availableRooms
              isPromoEligible
              promotions {
                typeId
                promotionDiscount {
                  value
                }
                isRatePlanAsPromotion
                cmsTypeId
                description
              }
              bookingDuration {
                unit
                value
              }
              supplierId
              corSummary {
                hasCor
                corType
                isOriginal
                hasOwnCOR
                isBlacklistedCor
              }
              localVoucher {
                currencyCode
                amount
              }
              pricing {
                currency
                price {
                  perNight {
                    exclusive {
                      display
                      cashbackPrice
                      displayAfterCashback
                      originalPrice
                    }
                    inclusive {
                      display
                      cashbackPrice
                      displayAfterCashback
                      originalPrice
                    }
                  }
                  perBook {
                    exclusive {
                      display
                      cashbackPrice
                      displayAfterCashback
                      rebatePrice
                      originalPrice
                      autoAppliedPromoDiscount
                    }
                    inclusive {
                      display
                      cashbackPrice
                      displayAfterCashback
                      rebatePrice
                      originalPrice
                      autoAppliedPromoDiscount
                    }
                  }
                  perRoomPerNight {
                    exclusive {
                      display
                      crossedOutPrice
                      cashbackPrice
                      displayAfterCashback
                      rebatePrice
                      pseudoCouponPrice
                      originalPrice
                      loyaltyOfferSummary {
                        basePrice {
                          exclusive
                          allInclusive
                        }
                        offers {
                          identifier
                          burn {
                            points
                            payableAmount
                          }
                          earn {
                            points
                          }
                          offerType
                          isSelected
                        }
                      }
                    }
                    inclusive {
                      display
                      crossedOutPrice
                      cashbackPrice
                      displayAfterCashback
                      rebatePrice
                      pseudoCouponPrice
                      originalPrice
                      loyaltyOfferSummary {
                        basePrice {
                          exclusive
                          allInclusive
                        }
                        offers {
                          identifier
                          burn {
                            points
                            payableAmount
                          }
                          earn {
                            points
                          }
                          offerType
                          isSelected
                        }
                      }
                    }
                  }
                  totalDiscount
                  priceAfterAppliedAgodaCash {
                    perBook {
                      ...Frag7hfd4bgjhjaa3j4ch1jd
                    }
                    perRoomPerNight {
                      ...Frag7hfd4bgjhjaa3j4ch1jd
                    }
                  }
                }
                apsPeek {
                  perRoomPerNight {
                    ...Fraga0abi1adjdee6711egi6
                  }
                }
                promotionPricePeek {
                  display {
                    perBook {
                      ...Fraga0abi1adjdee6711egi6
                    }
                    perRoomPerNight {
                      ...Fraga0abi1adjdee6711egi6
                    }
                    perNight {
                      ...Fraga0abi1adjdee6711egi6
                    }
                  }
                  discountType
                  promotionCodeType
                  promotionCode
                  promoAppliedOnFinalPrice
                  childPromotions {
                    campaignId
                  }
                  campaignName
                }
                channelDiscountSummary {
                  channelDiscountBreakdown {
                    display
                    discountPercent
                    channelId
                  }
                }
                promotionsCumulative {
                  promotionCumulativeType
                  amountPercentage
                  minNightsStay
                }
              }
              uid
              payment {
                cancellation {
                  cancellationType
                }
              }
              discount {
                deals
                channelDiscount
              }
              saveUpTo {
                perRoomPerNight
              }
              benefits {
                id
                targetType
              }
              channel {
                id
              }
              mseRoomSummaries {
                supplierId
                subSupplierId
                pricingSummaries {
                  currency
                  channelDiscountSummary {
                    channelDiscountBreakdown {
                      channelId
                      discountPercent
                      display
                    }
                  }
                  price {
                    perRoomPerNight {
                      exclusive {
                        display
                      }
                      inclusive {
                        display
                      }
                    }
                  }
                }
              }
              cashback {
                cashbackGuid
                showPostCashbackPrice
                cashbackVersion
                percentage
                earnId
                dayToEarn
                expiryDay
                cashbackType
                appliedCampaignName
              }
              agodaCash {
                showBadge
                giftcardGuid
                dayToEarn
                expiryDay
                percentage
              }
              corInfo {
                corBreakdown {
                  taxExPN {
                    ...Fraghi19f4d8j076gj4fah50
                  }
                  taxInPN {
                    ...Fraghi19f4d8j076gj4fah50
                  }
                  taxExPRPN {
                    ...Fraghi19f4d8j076gj4fah50
                  }
                  taxInPRPN {
                    ...Fraghi19f4d8j076gj4fah50
                  }
                }
                corInfo {
                  corType
                }
              }
              loyaltyDisplay {
                items
              }
              capacity {
                extraBedsAvailable
              }
              pricingMessages {
                formatted {
                  location
                  texts {
                    index
                    text
                  }
                }
              }
              campaign {
                selected {
                  campaignId
                  promotionId
                  messages {
                    campaignName
                    title
                    titleWithDiscount
                    description
                    linkOutText
                    url
                  }
                }
              }
              stayPackageType
            }
          }
        }
      }
      metaLab {
        attributes {
          attributeId
          dataType
          value
          version
        }
      }
      enrichment {
        topSellingPoint {
          tspType
          value
        }
        pricingBadges {
          badges
        }
        uniqueSellingPoint {
          rank
          segment
          uspType
          uspPropertyType
        }
        bookingHistory {
          bookingCount {
            count
            timeFrame
          }
        }
        showReviewSnippet
        isPopular
        roomInformation {
          cheapestRoomSizeSqm
          facilities {
            id
            propertyFacilityName
            symbol
          }
        }
      }
    }
    searchEnrichment {
      suppliersInformation {
        supplierId
        supplierName
        isAgodaBand
      }
    }
    aggregation {
      matrixGroupResults {
        matrixGroup
        matrixItemResults {
          id
          name
          count
          filterKey
          filterRequestType
          extraDataResults {
            text
            matrixExtraDataType
          }
        }
      }
    }
  }
}

fragment Frag7hfd4bgjhjaa3j4ch1jd on DisplayPrice {
  exclusive
  allInclusive
}

fragment Fraga0abi1adjdee6711egi6 on DFDisplayPrice {
  exclusive
  allInclusive
}

fragment Fraghi19f4d8j076gj4fah50 on DFCorBreakdownItem {
  price
  id
}
    """
    todays_Date = datetime.now()
 
    # Calling the isoformat() function over the
    # today's date and time
    DateTime_in_ISOFormat = todays_Date.isoformat()[:-3] + "Z"
    variable= {
  "CitySearchRequest": {
    "cityId": 14018,
    "searchRequest": {
      "searchCriteria": {
        "isAllowBookOnRequest": True,
        "bookingDate": DateTime_in_ISOFormat,
        "checkInDate": start_date,
        "localCheckInDate": start_date.split("T")[0],
        "los": 1,
        "rooms": 1,
        "adults": 1,
        "children": 0,
        "childAges": [],
        "ratePlans": [],
        "featureFlagRequest": {
          "newNumberOfBedroomsConfigFilter": False,
          "fetchNamesForTealium": True,
          "fiveStarDealOfTheDay": True,
          "isAllowBookOnRequest": False,
          "showUnAvailable": True,
          "showRemainingProperties": True,
          "isMultiHotelSearch": False,
          "enableAgencySupplyForPackages": True,
          "flags": [
            {
              "feature": "FamilyChildFriendlyPopularFilter",
              "enable": True
            },
            {
              "feature": "FamilyChildFriendlyPropertyTypeFilter",
              "enable": True
            },
            {
              "feature": "FamilyMode",
              "enable": False
            }
          ],
          "enablePageToken": False,
          "enableDealsOfTheDayFilter": False,
          "isEnableSupplierFinancialInfo": False,
          "ignoreRequestedNumberOfRoomsForNha": False
        },
        "isUserLoggedIn": False,
        "currency": "IDR",
        "travellerType": "Couple",
        "isAPSPeek": False,
        "enableOpaqueChannel": False,
        "isEnabledPartnerChannelSelection": None,
        "sorting": {
          "sortField": "Ranking",
          "sortOrder": "Desc",
          "sortParams": None
        },
        "requiredBasis": "PRPN",
        "requiredPrice": "Exclusive",
        "suggestionLimit": 0,
        "synchronous": False,
        "supplierPullMetadataRequest": None,
        "isRoomSuggestionRequested": False,
        "isAPORequest": False,
        "hasAPOFilter": False
      },
      "searchContext": {
        "userId": "3a57c139-5219-47df-847c-073572f2a12a",
        "memberId": 0,
        "locale": "en-us",
        "cid": 1844104,
        "origin": "ID",
        "platform": 1,
        "deviceTypeId": 1,
        "experiments": {
          "forceByVariant": None,
          "forceByExperiment": [
            {
              "id": "UMRAH-B2B",
              "variant": "B"
            },
            {
              "id": "UMRAH-B2C-REGIONAL",
              "variant": "B"
            },
            {
              "id": "UMRAH-B2C",
              "variant": "Z"
            },
            {
              "id": "JGCW-204",
              "variant": "B"
            }
          ]
        },
        "isRetry": False,
        "showCMS": False,
        "storeFrontId": 3,
        "pageTypeId": 103,
        "whiteLabelKey": None,
        "ipAddress": "202.43.94.43",
        "endpointSearchType": "CitySearch",
        "trackSteps": None,
        "searchId": "f7c2eee9-d5ab-4389-bfc2-7f6b14c41e45"
      },
      "matrix": None,
      "matrixGroup": [
        {
          "matrixGroup": "NumberOfBedrooms",
          "size": 100
        },
        {
          "matrixGroup": "LandmarkIds",
          "size": 10
        },
        {
          "matrixGroup": "GroupedBedTypes",
          "size": 100
        },
        {
          "matrixGroup": "RoomBenefits",
          "size": 100
        },
        {
          "matrixGroup": "AtmosphereIds",
          "size": 100
        },
        {
          "matrixGroup": "RoomAmenities",
          "size": 100
        },
        {
          "matrixGroup": "AffordableCategory",
          "size": 100
        },
        {
          "matrixGroup": "HotelFacilities",
          "size": 100
        },
        {
          "matrixGroup": "BeachAccessTypeIds",
          "size": 100
        },
        {
          "matrixGroup": "StarRating",
          "size": 20
        },
        {
          "matrixGroup": "AllGuestReviewBreakdown",
          "size": 100
        },
        {
          "matrixGroup": "MetroSubwayStationLandmarkIds",
          "size": 20
        },
        {
          "matrixGroup": "CityCenterDistance",
          "size": 100
        },
        {
          "matrixGroup": "ProductType",
          "size": 100
        },
        {
          "matrixGroup": "TripPurpose",
          "size": 5
        },
        {
          "matrixGroup": "BusStationLandmarkIds",
          "size": 20
        },
        {
          "matrixGroup": "IsSustainableTravel",
          "size": 2
        },
        {
          "matrixGroup": "ReviewLocationScore",
          "size": 3
        },
        {
          "matrixGroup": "LandmarkSubTypeCategoryIds",
          "size": 20
        },
        {
          "matrixGroup": "ReviewScore",
          "size": 100
        },
        {
          "matrixGroup": "AccommodationType",
          "size": 100
        },
        {
          "matrixGroup": "PaymentOptions",
          "size": 100
        },
        {
          "matrixGroup": "TrainStationLandmarkIds",
          "size": 20
        },
        {
          "matrixGroup": "HotelAreaId",
          "size": 100
        },
        {
          "matrixGroup": "HotelChainId",
          "size": 10
        },
        {
          "matrixGroup": "RecommendedByDestinationCity",
          "size": 10
        },
        {
          "matrixGroup": "Deals",
          "size": 100
        }
      ],
      "filterRequest": {
        "idsFilters": [],
        "rangeFilters": [],
        "textFilters": []
      },
      "page": {
        "pageSize": 45,
        "pageNumber": 1,
        "pageToken": ""
      },
      "apoRequest": {
        "apoPageSize": 10
      },
      "searchDetailRequest": {
        "priceHistogramBins": 50
      },
      "isTrimmedResponseRequested": False,
      "featuredAgodaHomesRequest": None,
      "featuredLuxuryHotelsRequest": None,
      "highlyRatedAgodaHomesRequest": {
        "numberOfAgodaHomes": 30,
        "minimumReviewScore": 7.5,
        "minimumReviewCount": 3,
        "accommodationTypes": [
          28,
          29,
          30,
          102,
          103,
          106,
          107,
          108,
          109,
          110,
          114,
          115,
          120,
          131
        ],
        "sortVersion": 0
      },
      "extraAgodaHomesRequest": None,
      "extraHotels": {
        "extraHotelIds": [
          idHotel
        ],
        "enableFiltersForExtraHotels": False
      },
      "packaging": None,
      "flexibleSearchRequest": {
        "fromDate": DateTime_in_ISOFormat.split("T")[0],
        "toDate": end_date_locale,
        "alternativeDateSize": 4,
        "isFullFlexibleDateSearch": False
      },
      "rankingRequest": {
        "isNhaKeywordSearch": False
      },
      "rocketmilesRequestV2": None,
      "featuredPulsePropertiesRequest": {
        "numberOfPulseProperties": 15
      }
    }
  },
  "ContentSummaryRequest": {
    "context": {
      "rawUserId": "3a57c139-5219-47df-847c-073572f2a12a",
      "memberId": 0,
      "userOrigin": "ID",
      "locale": "en-us",
      "forceExperimentsByIdNew": [
        {
          "key": "UMRAH-B2B",
          "value": "B"
        },
        {
          "key": "UMRAH-B2C-REGIONAL",
          "value": "B"
        },
        {
          "key": "UMRAH-B2C",
          "value": "Z"
        },
        {
          "key": "JGCW-204",
          "value": "B"
        }
      ],
      "apo": False,
      "searchCriteria": {
        "cityId": 14018
      },
      "platform": {
        "id": 1
      },
      "storeFrontId": 3,
      "cid": "1844104",
      "occupancy": {
        "numberOfAdults": 1,
        "numberOfChildren": 0,
        "travelerType": 3,
        "checkIn": start_date,
      },
      "deviceTypeId": 1,
      "whiteLabelKey": "",
      "correlationId": ""
    },
    "summary": {
      "highlightedFeaturesOrderPriority": None,
      "includeHotelCharacter": True
    },
    "reviews": {
      "commentary": None,
      "demographics": {
        "providerIds": None,
        "filter": {
          "defaultProviderOnly": True
        }
      },
      "summaries": {
        "providerIds": None, 
        "apo": True,
        "limit": 1,
        "travellerType": 3
      },
      "cumulative": {
        "providerIds": None
      },
      "filters": None
    },
    "images": {
      "page": None,
      "maxWidth": 0,
      "maxHeight": 0,
      "imageSizes": None,
      "indexOffset": None
    },
    "rooms": {
      "images": None,
      "featureLimit": 0,
      "filterCriteria": None,
      "includeMissing": False,
      "includeSoldOut": False,
      "includeDmcRoomId": False,
      "soldOutRoomCriteria": None,
      "showRoomSize": True,
      "showRoomFacilities": True,
      "showRoomName": False
    },
    "nonHotelAccommodation": True,
    "engagement": True,
    "highlights": {
      "maxNumberOfItems": 0,
      "images": {
        "imageSizes": [
          {
            "key": "full",
            "size": {
              "width": 0,
              "height": 0
            }
          }
        ]
      }
    },
    "personalizedInformation": False,
    "localInformation": {
      "images": None
    },
    "features": None,
    "rateCategories": True,
    "contentRateCategories": {
      "escapeRateCategories": {}
    },
    "synopsis": True
  },
  "PricingSummaryRequest": {
    "cheapestOnly": True,
    "context": {
      "isAllowBookOnRequest": True,
      "abTests": [
        {
          "testId": 9021,
          "abUser": "B"
        },
        {
          "testId": 9023,
          "abUser": "B"
        },
        {
          "testId": 9024,
          "abUser": "B"
        },
        {
          "testId": 9025,
          "abUser": "B"
        },
        {
          "testId": 9027,
          "abUser": "B"
        },
        {
          "testId": 9029,
          "abUser": "B"
        }
      ],
      "clientInfo": {
        "cid": 1844104,
        "languageId": 1,
        "languageUse": 1,
        "origin": "ID",
        "platform": 1,
        "searchId": "f7c2eee9-d5ab-4389-bfc2-7f6b14c41e45",
        "storefront": 3,
        "userId": "3a57c139-5219-47df-847c-073572f2a12a",
        "ipAddress": "202.43.94.43"
      },
      "experiment": [
        {
          "name": "UMRAH-B2B",
          "variant": "B"
        },
        {
          "name": "UMRAH-B2C-REGIONAL",
          "variant": "B"
        },
        {
          "name": "UMRAH-B2C",
          "variant": "Z"
        },
        {
          "name": "JGCW-204",
          "variant": "B"
        },
        {
          "name": "PFE-10385-KS",
          "variant": "B"
        }
      ],
      "sessionInfo": {
        "isLogin": False,
        "memberId": 0,
        "sessionId": 1
      },
      "packaging": None
    },
    "isSSR": True,
    "pricing": {
      "bookingDate": DateTime_in_ISOFormat,
      "checkIn": start_date,
      "checkout": end_date,
      "localCheckInDate": start_date_locale,
      "localCheckoutDate": end_date_locale,
      "currency": "IDR",
      "details": {
        "cheapestPriceOnly": False,
        "itemBreakdown": False,
        "priceBreakdown": False
      },
      "featureFlag": [
        "ClientDiscount",
        "PriceHistory",
        "VipPlatinum",
        "RatePlanPromosCumulative",
        "PromosCumulative",
        "CouponSellEx",
        "MixAndSave",
        "APSPeek",
        "StackChannelDiscount",
        "AutoApplyPromos",
        "EnableAgencySupplyForPackages",
        "EnableCashback",
        "CreditCardPromotionPeek",
        "EnableCofundedCashback",
        "DispatchGoLocalForInternational",
        "EnableGoToTravelCampaign"
      ],
      "features": {
        "crossOutRate": False,
        "isAPSPeek": False,
        "isAllOcc": False,
        "isApsEnabled": False,
        "isIncludeUsdAndLocalCurrency": False,
        "isMSE": True,
        "isRPM2Included": True,
        "maxSuggestions": 0,
        "isEnableSupplierFinancialInfo": False,
        "isLoggingAuctionData": False,
        "newRateModel": False,
        "overrideOccupancy": False,
        "filterCheapestRoomEscapesPackage": False,
        "priusId": 0,
        "synchronous": False,
        "enableRichContentOffer": True,
        "showCouponAmountInUserCurrency": False,
        "disableEscapesPackage": False,
        "enablePushDayUseRates": False,
        "enableDayUseCor": False
      },
      "filters": {
        "cheapestRoomFilters": [],
        "filterAPO": False,
        "ratePlans": [
          1
        ],
        "secretDealOnly": False,
        "suppliers": [],
        "nosOfBedrooms": []
      },
      "includedPriceInfo": False,
      "occupancy": {
        "adults": 1,
        "children": 0,
        "childAges": [],
        "rooms": 1,
        "childrenTypes": []
      },
      "supplierPullMetadata": {
        "requiredPrecheckAccuracyLevel": 0
      },
      "mseHotelIds": [],
      "ppLandingHotelIds": [],
      "searchedHotelIds": [],
      "paymentId": -1,
      "externalLoyaltyRequest": None
    },
    "suggestedPrice": "Exclusive"
  },
  "PriceStreamMetaLabRequest": {
    "attributesId": [
      8,
      1,
      18,
      7,
      11,
      2,
      3
    ]
  }
}
    headers={
        "authority":"www.agoda.com",
"accept":"*/*",
"accept-language":"en-US,en;q=0.9",
"access-control-max-age":"7200",
"ag-analytics-session-id":"5361130425791025062",
"ag-correlation-id":"553c33a9-3e38-45ae-9806-7f91de1ec82d",
"ag-debug-override-origin":"ID",
"ag-language-locale":"en-us",
"ag-page-type-id":"103",
"ag-request-attempt":"1",
"ag-request-id":"73170da3-33d5-468d-93f3-2ab9d106caa2",
"ag-retry-attempt":"0",
"cache-control":"no-cache",
"content-type":"application/json",
"cookie":"agoda.analytics=Id=5836282345757306058&Signature=1733972267166371221&Expiry=1700678990213; agoda.familyMode=Mode=0; agoda.prius=PriusID=0&PointsMaxTraffic=Agoda; agoda.user.03=UserId=aa56f34e-a94e-4499-aa59-a64889aa4b22",
"dnt":"1",
"origin":"https://www.agoda.com",
"pragma":"no-cache",
"sec-ch-ua-mobile":"?0",
"sec-ch-ua-platform":"Windows",
"sec-fetch-dest":"empty",
"sec-fetch-mode":"cors",
"sec-fetch-site":"same-origin",
"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"
    }

    url = "https://www.agoda.com/graphql/search"
    print(DateTime_in_ISOFormat)
    print(start_date)
    print(end_date)
    print(start_date_locale)
    print(end_date_locale)
    print(idHotel)
    result = send_request(url, headers, "POST", payload={
        "query": query, "variables": variable
    })
    return result

    # do stuff
